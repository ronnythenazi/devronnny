from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from .forms import SignUpFrm, UsrUpdateFrm, UpdatePasswordFrm
from magazine.models import Profile
from magazine.blogpublishing import frmProfile

class CreateProfile(generic.CreateView):
    model = Profile
    form_class = frmProfile
    template_name = "registration/createProfile.html"
    success_url  = reverse_lazy('magazine:magazineNews')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
"""
class updateProfileV(generic.UpdateView):
    model = Profile
    #form_class = frmProfile
    template_name = 'registration/update_profile.html'
    fields = ['bio', 'profile_img']
    success_url = reverse_lazy('magazine:magazineNews')

"""
def updateProfileV(request, id):
    obj = get_object_or_404(Profile, id = id)
    frm = frmProfile(request.POST or None, request.FILES or None, instance = obj)
    if(request.method == 'POST'):
        if frm.is_valid():
            frm.save()
            return redirect('magazine:magazineNews')
    return render(request, 'registration/update_profile.html', {'form':frm , 'obj':obj})


class SignUp(generic.CreateView):
    form_class = SignUpFrm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')

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

# Create your views here.
