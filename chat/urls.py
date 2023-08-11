from django.urls import path, include
#from magazine import urls
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import  get_private_chat_users_details

app_name = 'chat'

urlpatterns = [

path('private-chat-users-details', get_private_chat_users_details, name="private-chat-users-details"),




]
