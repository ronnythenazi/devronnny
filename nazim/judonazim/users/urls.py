from django.urls import path, include
from .views import SignUp, ProfileUpdateView

app_name = 'users'
urlpatterns = [
    path('SignUp/', SignUp.as_view(), name = "SignUp"),
    path('profile/', ProfileUpdateView.as_view(), name = "profile_ctl"),
]
