from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy, reverse
from .forms import SignUpFrm, UsrUpdateFrm, UpdatePasswordFrm, SignInFrm
from magazine.models import Profile, Album
from magazine.blogpublishing import frmProfile
from magazine.decorations import add_def_group_if_not_exist
from django.contrib.auth.models import Group, User
from django.contrib import messages
from django.forms import inlineformset_factory, modelformset_factory
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth import (authenticate, get_user_model, login, logout,)

from django.utils.encoding import force_bytes, force_text, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from .utils import token_generator
from django.template.loader import get_template
from django.template import Context

from django.views import View
#from general.txt_handler import get_txt_from_file, get_mail_msg

def login_view(request):
    form = SignInFrm(request.POST or None)
    if request.method == 'POST':
        if not form.is_valid():  # Here
            return render(request, 'users/signin.html', {'form': form})
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('magazine:magazineNews')

        return HttpResponseRedirect("/SignIn")
    else:
        return render(request, 'users/signin.html', {'form': form})


class CreateProfile(generic.CreateView):
    model = Profile
    form_class = frmProfile
    template_name = "registration/createProfile.html"
    success_url  = reverse_lazy('magazine:magazineNews')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
"""
def updateProfileV(request, id):
    obj = get_object_or_404(Profile, id = id)
    frm = frmProfile(request.POST or None, request.FILES or None, instance = obj)
    if(request.method == 'POST'):
        if frm.is_valid():
            frm.save()
            return redirect('magazine:magazineNews')
    return render(request, 'registration/update_profile.html', {'form':frm , 'obj':obj})
"""
def updateProfileV(request, id):
    fields = ['description', 'myfile']
    profile_obj = get_object_or_404(Profile, id = id) #profile obj
    album_formset_factory = inlineformset_factory(Profile, Album,can_order = True,  extra=0, min_num=1, fields = ['description', 'myfile'])
    album_formset  = album_formset_factory(request.POST or None, request.FILES or None, instance=profile_obj)
    frm = frmProfile(request.POST or None, request.FILES or None, instance = profile_obj)
    if request.method == 'POST':
        if frm.is_valid():
            frm.save()
        if album_formset.is_valid():
            album_formset.save()
            return redirect('magazine:magazineNews')
        else:
            print(album_formset.errors)

    return render(request, 'registration/update_profile.html', {'album_formset':album_formset, 'form':frm, 'profile_obj':profile_obj})






@add_def_group_if_not_exist(def_group = 'members')
def SignUp(request):

    form = SignUpFrm(request.POST or None)
    if form.is_valid():
        usr = form.save(commit = False)
        password = form.cleaned_data.get('password')
        usr.set_password(password)
        usr.is_active = False
        usr.save()

        group = Group.objects.get(name = 'members')
        usr.groups.add(group)

        subject = 'message from judonazism, please verfiy your mail'
        #path to view
        # -  getting our curr domain
        # -  relative url to verification
        # -  encode uid
        # -  token

        uidb64 = urlsafe_base64_encode(force_bytes(usr.pk))
        domain  = get_current_site(request).domain
        link = reverse('users:activation', kwargs={'uidb64':uidb64, 'token':token_generator.make_token(usr)})
        active_url = 'http://' + domain + link

        #body = 'Hello ' + usr.username + ' Please use this link to verify your account\n' + active_url

        msg_htmly = get_template('general/verify_account_msg.html')
        msg_plaintext = get_template('general/verify_account_msg.txt')
        dict =  {'username':usr.username, 'active_url':active_url}
        text_content = msg_plaintext.render(dict)
        html_content = msg_htmly.render(dict)

        email = EmailMultiAlternatives(
            subject,
            text_content,
            'noreply@semycolon.com',
            [usr.email],
         )
        email.attach_alternative(html_content, "text/html")
        email.send(fail_silently=False)

        new_usr = authenticate(username = usr.username, password = password)
        #login(request, usr)
        return render(request, 'users/signup.html', {'form' :form, 'no_error':'true'})
        #return redirect('magazine:magazineNews')

    template_name = 'users/signup.html'
    return render(request, template_name, {'form' :form, 'no_error':'false'})

class verificationView(View):
    def get(self, request, uidb64, token):
        try:
            print('try to decode')
            id = force_text(urlsafe_base64_decode(uidb64))
            print('decode done')
            print('decode id is ' + str(id))
            user = User.objects.get(pk=id)
            print('user is ' + str(user))

            #check if linke was already activated before
            if not token_generator.check_token(user, token):
                #this mean user click the linke before
                print('print linked already pressed before')
                return redirect('users:SignIn')
                #return redirect('magazine:magazineNews')
            print('is actovate?')
            if user.is_active:
                return redirect('users:SignIn')
                #return redirect('magazine:magazineNews')
            user.is_active = True
            print('before save')
            user.save()
            print('saved')

            messages.success(request, 'Account activated successfully')
            print('message')
            return redirect('users:SignIn')
            #return redirect('magazine:magazineNews')

        except Exception as e:
            return redirect('magazine:magazineNews')




class accountUpdateView(generic.UpdateView):
    form_class = UsrUpdateFrm
    template_name = 'registration/update_account.html'
    success_url = reverse_lazy('magazine:magazineNews')

    def get_object(self):
        return self.request.user

class ChangePasswordV(PasswordChangeView):
    form_class = UpdatePasswordFrm
    template_name = 'registration/change-password.html'
    success_url = reverse_lazy('magazine:magazineNews')
