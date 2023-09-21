from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, Http404, redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect as http_response_redirect, JsonResponse
from django.utils.dateparse import parse_datetime
from users.members import get_profile_info_nick_or_user
from django.contrib.auth.models import User
from asgiref.sync import sync_to_async, async_to_sync
from django.db.models import Q

# Create your views here.

from django.contrib.auth import get_user_model

from .models import Chat, Message, ChatMsgNotification, chatType
from users.models import Contact

from django.db.models import Count

from .myNotifications import fetchNextNotifications

def fetchNextNotificationsAjax(request):
    if request.user.is_authenticated == False:
        return JsonResponse({'status':'not-log-in'})
    if not request.is_ajax or not request.method == "GET":
        return JsonResponse({'status':'not ajax get'})
    currNumofNotifications = int(request.GET.get('numofNotifications'))
    maxNotifications       = int(request.GET.get('maxNotifications'))
    nextNotifications = fetchNextNotifications(request.user, currNumofNotifications, maxNotifications)
    return JsonResponse(nextNotifications, safe=False)



User = get_user_model()

def get_login_user_rooms_ajax(request):
    if request.user.is_authenticated == False:
        return JsonResponse({'status':'not-log-in'})
    if not request.is_ajax or not request.method == "GET":
        return JsonResponse({'status':'not ajax get'})
    user = request.user
    contact = Contact.objects.get(user=user)
    chats = contact.chats.all()
    rooms = []
    for chat in chats:
        rooms.append({'chatId':str(chat.id), 'roomName':chat.chat_name})
    return JsonResponse(rooms, safe=False)




def get_or_create_personal_chat_room_ajax(request):

    if request.user.is_authenticated == False:
        return JsonResponse({'status':'not-log-in'})



    if request.is_ajax and request.method == "GET":
        chat_owner_username = request.GET.get('username_starter')
        to_username = request.GET.get('username_reciever')

        if request.user.username != chat_owner_username:
            return JsonResponse({'status':'not_authenticated'})

        user_owner = get_object_or_404(User, username=chat_owner_username)
        contact_owner_tuple = Contact.objects.get_or_create(user=user_owner)
        contact_owner = contact_owner_tuple[0]
        contact_owner_created = contact_owner_tuple[1]



        user_reciever = get_object_or_404(User, username=to_username)

        contact_reciever_tuple = Contact.objects.get_or_create(user=user_reciever)
        contact_reciever = contact_reciever_tuple[0]
        contact_reciever_created = contact_reciever_tuple[1]





        #rooms = Chat.objects.annotate(participants_count=Count('participants', distinct=True)).filter(participants_count = 2)

        #rooms = Chat.objects.annotate(participants_count=Count('participants', distinct=True)).filter(Q(participants_count__gte=1) & Q(participants_count__lte=2))


        user_chats = contact_owner.chats.filter(chatType = chatType['personal'])

        if (chat_owner_username == to_username):


            for chat in user_chats:
                if chat.participants.all().count() != 1:
                    continue
                chat_id = str(chat.id)
                chat_name = str(chat.chat_name)
                return JsonResponse({'status':'success', 'chatId':chat_id, 'roomName': chat_name})

            chat = Chat.objects.create()

            chat_id = str(chat.id)
            chat_name = 'Chat' + str(chat_id)
            chat.chat_name = chat_name
            chat.save()
            chat.participants.add(contact_owner)


        for chat in user_chats:

            if chat.participants.all().count() != 2:
                continue
            is_reciever_exist = False
            is_chat_owner_exist = False

            if(chat.participants.filter(user = user_reciever).exists()):
                is_reciever_exist = True

            if(chat.participants.filter(user = user_owner).exists()):
                is_chat_owner_exist = True

            if(is_reciever_exist and is_chat_owner_exist):
                chat_id = str(chat.id)
                chat_name = str(chat.chat_name)
                return JsonResponse({'status':'success', 'chatId':chat_id, 'roomName': chat_name})


        chat = Chat.objects.create()

        chat_id = str(chat.id)
        chat_name = 'Chat' + str(chat_id)
        chat.chat_name = chat_name
        chat.save()
        chat.participants.add(contact_owner)

        chat.participants.add(contact_reciever)



        return JsonResponse({'status':'success', 'chatId':chat_id, 'roomName': chat_name})










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




@sync_to_async
def save_message_for_chat(current_chat, user_contact, content):
    message = Message.objects.create(
        contact=user_contact,
        content=content,
        chat = current_chat)


    return message


@sync_to_async
def save_chat_msg_notification(current_chat, message):
    notification = ChatMsgNotification.objects.create(chat = current_chat, message = message)
    return notification


@sync_to_async
def is_authorize_to_private_chat(ws, roomName):
    log_in_user = ws.scope["user"].username

    #if log in user is allow\belong to this private chat
    return is_login_user_in_particpants(log_in_user, roomName)
        #not authorize




def is_login_user_in_particpants(username, roomName):
    chat = get_object_or_404(Chat, chat_name=roomName)
    if chat.participants.filter(user__username = username).exists():
        return True
    return False

@sync_to_async
def get_last_messages(chatId):
    chat = get_object_or_404(Chat, id=chatId)
    return reversed(chat.messages.order_by('-timestamp').all()[:1000])

@sync_to_async
def get_user_contact(username):
    user = get_object_or_404(User, username=username)
    return get_object_or_404(Contact, user=user)

@sync_to_async
def get_current_chat(chatId):
    return get_object_or_404(Chat, id=chatId)


@sync_to_async
def get_participants_for_chat(chatId):
    result = []
    chat = get_object_or_404(Chat, id=chatId)

    for contact in chat.participants.all():
        username = contact.user.username
        result.append({'username':username})
    return result



@sync_to_async
def messages_to_json(messages):
    result = []

    for message in messages:
        result.append(message_to_json(message))
    return result


def message_to_json(message):

    info =  get_profile_info_nick_or_user(message.contact.user)

    avatar = info['avatar']
    name   = info['name']

    dict = {
        'id': str(message.id),
        'author': message.contact.user.username,
        'content': str(message.content),
        'timestamp': str(message.timestamp),
        'avatar'   : avatar,
        'name'     : name,
    }

    return dict

@sync_to_async
def message_to_json_called_from_async(message):
    return message_to_json(message)

@sync_to_async
def get_user_avatar_and_name(user):
    info =  get_profile_info_nick_or_user(user)
    return info


    #return asyncio.run(get_chat_msg_dict_json(message))
