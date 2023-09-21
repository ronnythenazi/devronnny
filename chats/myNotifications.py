from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, Http404, redirect
from django.urls import reverse
from django.http import HttpResponse
from django.utils.dateparse import parse_datetime
from users.members import get_profile_info_nick_or_user
from django.contrib.auth.models import User
from .models import Chat, ChatMsgNotification, Message
from users.models import Contact
from general.time import FriendlyTimePassedView
from django.db.models import Max
from django.db.models import Q




def getNextNotifications(user, currNumOfNotifications, maxNotifications):
    start = currNumOfNotifications
    end   = start + maxNotifications
    contact = Contact.objects.get(user = user)
    dict = Message.objects.filter(chat__in = contact.chats.all()).exclude(contact = contact).values('chat__id').distinct().annotate(last_msg_time=Max('timestamp')).order_by('-last_msg_time')[start:end]


    notifications =  []
    for i in dict:
        last_msg = Chat.objects.get(id = i['chat__id']).messages.exclude(contact = contact).order_by('timestamp').last()
        notifications.append(last_msg)


    notifications.reverse()
    return notifications


def fetchNextNotifications(user, currNumOfNotifications, maxNotifications=4):
    result = getNextNotifications(user, currNumOfNotifications, maxNotifications)
    notifications = []
    for i in result:
        chat = getChatOfMessage(i)
        author = get_profile_info_nick_or_user(i.contact.user)
        details = {}
        details['avatar']               = author['avatar'] #str(i.contact.user.profile.profile_img.url)
        details['author_name']          = author['name']
        details['author']               = i.contact.user.username
        details['content']              = i.content
        details['time_passed']          = FriendlyTimePassedView(i.timestamp)
        details['chatId']               = str(chat.id)
        details['roomName']             = chat.chat_name;
        notifications.append(details)
    notifications.reverse()
    return notifications

def getChatOfMessage(message):
    notification = ChatMsgNotification.objects.get(message = message)
    chat = notification.chat
    return chat
