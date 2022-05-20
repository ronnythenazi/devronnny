from django.urls import path, include
from .views import (SignUp, verificationView, accountUpdateView, ChangePasswordV,
updateProfileV, CreateProfile, login_view,
create_new_password, mail_for_password_recovery)
from django.contrib.auth import views as auth_views

app_name = 'users'
urlpatterns = [
    #path('SignUp/', SignUp.as_view(), name = "SignUp"),
    path('SignUp/', SignUp, name = "SignUp"),
    path('profile/', accountUpdateView.as_view(), name = "profile_ctl"),
    path('password/', ChangePasswordV.as_view(), name = "change-password"),
    path('<int:id>/profileUpdate/', updateProfileV, name = "UpdateProfile"),
    path('profile-setting/', CreateProfile.as_view(), name = "CreateProfile"),
    path('SignIn/', login_view, name="SignIn"),
    path('activation/<uidb64>/<token>', verificationView.as_view(), name = 'activation'),
    path('forget-password-mail/',mail_for_password_recovery , name="forget-password-mail"),
    path('create-new-password/<uidb64>/<token>',create_new_password, name="create-new-password"),

]
