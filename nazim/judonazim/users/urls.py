from django.urls import path, include
from .views import SignUp, ProfileUpdateView, ChangePasswordV
from django.contrib.auth import views as auth_views

app_name = 'users'
urlpatterns = [
    path('SignUp/', SignUp.as_view(), name = "SignUp"),
    path('profile/', ProfileUpdateView.as_view(), name = "profile_ctl"),
    #path('password/', auth_views.PasswordChangeView.as_view(template_name = 'registration/change-password.html'), name = "change-password"),
    path('password/', ChangePasswordV.as_view(), name = "change-password"),
]
