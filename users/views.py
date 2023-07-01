from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy, reverse
from .forms import (SignUpFrm, UsrUpdateFrm, UpdatePasswordFrm,
SignInFrm, mail_for_password_recovery_frm, CreatePasswordFrm)
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
from .utils import token_generator, token_generator_general
from django.template.loader import get_template
from django.template import Context
from .members import is_username_active

from django.views import View

import threading



class EmailThread(threading.Thread):
    def __init__(self, email):
        self.EmailMultiAlternatives = email
        threading.Thread.__init__(self)

    def run(self):
        self.EmailMultiAlternatives.send(fail_silently=True)

def login_view(request):
    form = SignInFrm(request.POST or None)
    if request.method == 'POST':
        if not form.is_valid():  # Here
            return render(request, 'users/signin.html', {'form': form})
        username_input = request.POST['username']
        password = request.POST['password']
        #user = authenticate(username=username, password=password)
        #if is_username_active(username):
        username = None
        try:
            user_obj = User.objects.filter(email=username_input)[0]
            username = user_obj.username
            user = authenticate(username=username, password=password)
        except:
            username = username_input
            user = authenticate(username=username, password=password)

        if is_username_active(username):
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



def mail_for_password_recovery(request):
    form = mail_for_password_recovery_frm(request.POST or None)
    if form.is_valid():
        body_template_name = 'restore_password'
        subject = 'message from judonazism, restore your password'
        email = request.POST.get('email')
        user = User.objects.filter(email=email)[0]
        url_to_go = "users:create-new-password"
        create_and_send_activation_link(body_template_name, subject, user, url_to_go, request)
        return render(request, 'registration/mail_for_password_recovery.html', {'form' :form, 'no_error':'true'})
    return render(request, 'registration/mail_for_password_recovery.html', {'form' :form, 'no_error':'false'})

def create_and_send_activation_link(body_template_name, subject, user, url_to_go, request):
    active_url = create_activation_link(user, url_to_go, request)
    msg_htmly = get_template('general/' + body_template_name + '.html')
    msg_plaintext = get_template('general/' + body_template_name + '.txt')
    dict =  {'username':user.username, 'active_url':active_url}
    text_content = msg_plaintext.render(dict)
    html_content = msg_htmly.render(dict)

    email = EmailMultiAlternatives(
        subject,
        html_content,
        'activate@em5210.ronnywasright.com',
        [user.email],
     )
    email.attach_alternative(html_content, "text/html")
    #email.send(fail_silently=True)

    EmailThread(email).start()



def create_activation_link(user, url_to_go, request):
    uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
    domain  = get_current_site(request).domain
    link = reverse(url_to_go, kwargs={'uidb64':uidb64, 'token':token_generator_general.make_token(user)})
    active_url = 'http://' + domain + link
    return active_url


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
             html_content,
             'signup@em5210.ronnywasright.com',
             [usr.email],
          )
        email.attach_alternative(html_content, "text/html")
        #email.send(fail_silently=True)
        EmailThread(email).start()


        new_usr = authenticate(username = usr.username, password = password)
        #login(request, usr)
        return render(request, 'users/signup.html', {'form' :form, 'no_error':'true'})
        #return redirect('magazine:magazineNews')

    template_name = 'users/signup.html'
    return render(request, template_name, {'form' :form, 'no_error':'false'})

def create_new_password(request, uidb64, token):
    try:

        id = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=id)
        print('user resotre passowrd name' + user.username)


        if not token_generator_general.check_token(user, token):


            return redirect('users:SignIn')


        template_name = 'registration/create_new_password.html'
        form = CreatePasswordFrm(request.POST or None)
        if request.method == 'POST':
            if not form.is_valid():
                return render(request, template_name, {'form':form} )
            password = form.cleaned_data.get('new_password2')
            user.set_password(password)
            user.save()
            login_user = authenticate(username=user.username, password=password)

            if is_username_active(user.username):
                login(request, login_user)
                return redirect('magazine:magazineNews')

        return render(request, template_name, {'form':form} )


    except Exception as e:
        return redirect('magazine:magazineNews')



class verificationView(View):
    def get(self, request, uidb64, token):
        try:
            id = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=id)

            #check if linke was already activated before
            if not token_generator.check_token(user, token):
                #this mean user click the linke before
                return redirect('users:SignIn')
                #return redirect('magazine:magazineNews')
            if user.is_active:
                return redirect('users:SignIn')
                #return redirect('magazine:magazineNews')
            user.is_active = True
            user.save()

            messages.success(request, 'Account activated successfully')
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
