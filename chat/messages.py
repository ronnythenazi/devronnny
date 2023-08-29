from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, Http404, redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.utils.dateparse import parse_datetime
from users.members import get_profile_info_nick_or_user
from django.contrib.auth.models import User
from .models import Chat, ChatMsgNotification
from users.models import Contact



def show_last_notifications(user):
    contact = Contact.objects.get(user = user)
    notifications = ChatMsgNotification.objects.filter(chat__in = contact.chats).exclude(message__in = contact.messages)



def is_user_permitted_for_chat(user, chatId):
    chat = Chat.objects.get(id = chatId)
    return chat.participants.filter(user = user).exists()


def is_it_my_notification(msg_notification, username):
    sent_to = msg_notification.get_to_username()
    if sent_to != username:
        return False
    return True
