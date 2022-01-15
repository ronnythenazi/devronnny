from django.urls import path, include
from .views import SignUp, accountUpdateView, ChangePasswordV, updateProfileV, CreateProfile, login_view
from django.contrib.auth import views as auth_views

app_name = 'users'
urlpatterns = [
    #path('SignUp/', SignUp.as_view(), name = "SignUp"),
    path('SignUp/', SignUp, name = "SignUp"),
    path('profile/', accountUpdateView.as_view(), name = "profile_ctl"),
    path('password/', ChangePasswordV.as_view(), name = "change-password"),
    path('<int:id>/profileUpdate/', updateProfileV, name = "UpdateProfile"),
    path('profile-setting/', CreateProfile.as_view(), name = "CreateProfile"),
    path('SignIn/', login_view, name="SignIn")

]
