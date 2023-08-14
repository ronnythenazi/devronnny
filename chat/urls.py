from django.urls import path, include
#from magazine import urls
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import  get_private_chat_users_details, get_or_create_private_chat_room_ajax

app_name = 'chat'

urlpatterns = [

path('private-chat-users-details', get_private_chat_users_details, name="private-chat-users-details"),
path('unique-chat-room', get_or_create_private_chat_room_ajax, name="get-or-generate-chatid"),




]
