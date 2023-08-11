from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, Http404, redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.utils.dateparse import parse_datetime
from users.members import get_profile_info_nick_or_user
from django.contrib.auth.models import User
from asgiref.sync import async_to_sync

# Create your views here.

from django.contrib.auth import get_user_model

from .models import Chat, Message
from users.models import Contact


User = get_user_model()




def get_private_chat_users_details(request):

    if request.user.is_authenticated == False:
        return JsonResponse([{'status':'not-log-in'}, {'status':'not-log-in'}], safe=False)

    #0 index for sender, 1 index for reviver
    people = []
    info = get_profile_info_nick_or_user(request.user)
    info.update({'status':'log-in'})
    people.append(info)
    if request.is_ajax and request.method == "GET":
        to_username = request.GET.get('to_username')
        user = User.objects.get(username = to_username)
        info = get_profile_info_nick_or_user(user)
        info.update({'status':'log-in'})
        people.append(info)


        return JsonResponse(people, safe=False)





def save_message_for_chat(current_chat, user_contact, content):
    message = Message.objects.create(
        contact=user_contact,
        content=content)

    current_chat.messages.add(message)
    current_chat.save()

    return message


def get_or_create_private_chat_room(chat_owner_username, to_username):
    user_owner = get_object_or_404(User, username=chat_owner_username)

    contact_owner_tuple = Contact.objects.get_or_create(user=user_owner)
    contact_owner = contact_owner_tuple[0]
    contact_owner_created = contact_owner_tuple[1]

    user_reciver = get_object_or_404(User, username=to_username)

    contact_reciver_tuple = Contact.objects.get_or_create(user=user_reciver)
    contact_reciver = contact_reciver_tuple[0]
    contact_reciver_created = contact_reciver_tuple[1]

    #contact_owner.friends.add(contact_reciver)

    #contact_reciver.friends.add(contact_owner)


    rooms = Chat.objects.all()


    for room in rooms:

        is_reciver_exist = False
        is_chat_owner_exist = False

        if(room.participants.filter(user = user_reciver).exists()):
            is_reciver_exist = True

        if(room.participants.filter(user = user_owner).exists()):
            is_chat_owner_exist = True


        if(is_reciver_exist and is_chat_owner_exist):

           chat = room

           chat_id = str(chat.id)

           return chat_id

    chat_name = 'private-chat-' + user_owner.username + '-to-' +  user_reciver.username
    chat = Chat.objects.create(chat_name = chat_name)

    chat.participants.add(contact_owner)

    chat.participants.add(contact_reciver)

    chat_id = str(chat.id)

    return chat_id



















def get_last_messages(chatId):
    chat = get_object_or_404(Chat, id=chatId)
    return chat.messages.order_by('-timestamp').all()[:10]


def get_user_contact(username):
    user = get_object_or_404(User, username=username)
    return get_object_or_404(Contact, user=user)


def get_current_chat(chatId):
    return get_object_or_404(Chat, id=chatId)
