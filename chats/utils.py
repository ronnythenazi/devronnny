from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, Http404, redirect
from django.urls import reverse
from django.http import HttpResponse, JsonResponse
from django.utils.dateparse import parse_datetime
from users.members import get_profile_info_nick_or_user
from django.contrib.auth.models import User
from .models import Chat, ChatMsgNotification
from users.models import Contact
from general.time import FriendlyTimePassedView
from django.conf import settings



from webpush import send_user_notification
from asgiref.sync import sync_to_async
from django.template.loader import get_template

# this time author is a user object(i.e, not username)

@sync_to_async
def send_chat_webpush_notification_called_from_async(chatId, author, msg):
    chat = Chat.objects.get(id = chatId)
    author_info = get_profile_info_nick_or_user(author)
    author_avatar = author_info['avatar']
    author_name   = author_info['name']
    for participant in chat.participants.all():
        # participant is a contact object
        user = participant.user
        username = user.username
        if author.username == username:
            continue

        participant_info = get_profile_info_nick_or_user(user)



        site_url = settings.SITE_URL
        dict = {'author_avatar':author_avatar, 'author_name':author_name, 'msg_content':msg, 'push_link':site_url}


        content = author_name + ":" + msg
        head =  get_template('chat/files/webpush_recieve_chat_msg.html').render()
        payload = {"head": head, 'body':content, "icon":author_avatar, 'url':site_url}



        send_user_notification(user=user, payload=payload, ttl=1000)
