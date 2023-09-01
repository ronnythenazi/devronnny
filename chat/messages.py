from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, Http404, redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.utils.dateparse import parse_datetime
from users.members import get_profile_info_nick_or_user
from django.contrib.auth.models import User
from .models import Chat, ChatMsgNotification
from users.models import Contact
from general.time import FriendlyTimePassedView



def show_last_notifications(user, max_messages):
    contact = Contact.objects.get(user = user)
    qs = ChatMsgNotification.objects.filter(chat__in = contact.chats.all()).exclude(message__in = contact.messages.all()).order_by('-message__timestamp')
    qs_lst = list(qs)
    notifications = set()
    chats = set()
    for i in qs_lst:
        chats.add(i.chat)
        notifications.add(i.chat.messages.exclude(contact  = contact).order_by('-timestamp').first())
        if(len(notifications)==max_messages):
            break
    return notifications


def notifications_minimal_view(user):
    result = show_last_notifications(user, 4)
    notifications = []
    for i in result:
        chat = get_chat_of_message(i)
        author = get_profile_info_nick_or_user(i.contact.user)
        details = {}
        details['avatar']               = author['avatar'] #str(i.contact.user.profile.profile_img.url)
        details['author_name']          = author['name']
        details['content']              = i.content
        details['time_passed']          = FriendlyTimePassedView(i.timestamp)
        details['chatId']               = str(chat.id)
        details['roomName']             = chat.chat_name;
        notifications.append(details)
    notifications.reverse()
    return notifications

def get_chat_of_message(message):
    notification = ChatMsgNotification.objects.get(message = message)
    chat = notification.chat
    return chat
