from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from .forms import SignUpFrm, UsrUpdateFrm, UpdatePasswordFrm, SignInFrm
from magazine.models import Profile, Album
from magazine.blogpublishing import frmProfile
from magazine.decorations import add_def_group_if_not_exist
from django.contrib.auth.models import Group
from django.contrib import messages
from django.forms import inlineformset_factory, modelformset_factory

from django.contrib.auth import (authenticate, get_user_model, login, logout,)

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
        usr.save()
        group = Group.objects.get(name = 'members')
        usr.groups.add(group)
        new_usr = authenticate(username = usr.username, password = password)
        login(request, usr)
        return redirect('magazine:magazineNews')

    template_name = 'users/signup.html'
    return render(request, template_name, {'form' :form})



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
