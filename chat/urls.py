from django.urls import path, include
#from magazine import urls
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import  (get_private_chat_users_details, get_or_create_personal_chat_room_ajax,
get_login_user_rooms_ajax,
)

app_name = 'chat'

urlpatterns = [

path('private-chat-users-details', get_private_chat_users_details, name="private-chat-users-details"),
path('unique-chat-room-for-personal-chat', get_or_create_personal_chat_room_ajax, name="get-or-generate-chatid-for-personal-chat"),
path('get-login-user-rooms',get_login_user_rooms_ajax,name='get_login_user_rooms')


]
