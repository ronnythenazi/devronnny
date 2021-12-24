from django.urls import path, include
from .views import SignUp

app_name = 'users'
urlpatterns = [
    path('SignUp/', SignUp.as_view(), name = "SignUp"),
]
