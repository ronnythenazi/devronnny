from django.urls import path, include
from .views import (SignUp, verificationView, accountUpdateView, ChangePasswordV,
updateProfileV, CreateProfile, login_view,
create_new_password, mail_for_password_recovery,
get_public_profile_page, get_user_snippet_info_ajax,
user_online_status_ajax,get_user_public_profile_url_ajax,get_public_profile_url_from_user_id_ajax,
getProfilePageforUsername_ajax, getUserTokensAjax, getUserPublicTokenAjax,
)
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
    path('public-profile/<int:id>/', get_public_profile_page, name = "public-profile"),
    path('get-user-snippet-info/', get_user_snippet_info_ajax, name = "user-snippet-info"),
    path('user-online-status', user_online_status_ajax, name='check-user-online-status'),
    path('user-public-profile-url',get_user_public_profile_url_ajax, name='get-user-public-profile-url'),
    path('public-profile-url-from-user-id',get_public_profile_url_from_user_id_ajax ,name='public-profile-url-from-user-id'),
    path('public-profile-url-from-username',getProfilePageforUsername_ajax ,name='public-profile-url-from-username'),
    path('UserToken', getUserTokensAjax, name="user-tokens"),
    path('UserPublicToken', getUserPublicTokenAjax, name="user-public-token"),
]
