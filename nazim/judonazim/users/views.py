from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.urls import reverse_lazy
from .forms import SignUpFrm

class SignUp(generic.CreateView):
    form_class = SignUpFrm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')

class ProfileUpdateView(generic.UpdateView):
    form_class = UserChangeForm
    template_name = 'registration/update_profile.html'
    success_url = reverse_lazy('magazine:magazineNews')

    def get_object(self):
        return self.request.user

# Create your views here.
