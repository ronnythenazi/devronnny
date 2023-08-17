from django.contrib.auth import get_user_model
from asgiref.sync import sync_to_async, async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json
from .models import Message, Chat
from users.models import Contact
from .views import (get_last_messages, get_user_contact, get_current_chat
, save_message_for_chat, messages_to_json, message_to_json_called_from_async, is_authorize_to_private_chat
,get_user_avatar_and_name,
)
from users.members import get_profile_info_nick_or_user

from channels.generic.websocket import AsyncWebsocketConsumer
import asyncio
import nest_asyncio
nest_asyncio.apply()

User = get_user_model()



class ChatNotifications(AsyncWebsocketConsumer):


    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f"notifications_{self.room_name}"
        await self.channel_layer.group_add(self.room_group_name,self.channel_name)

        await self.accept()


    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name,self.channel_name)


    async def notify_user(self, data):
        chatId = data['chatId']
        roomName = data['roomName']
        author   = data['author']
        avatar   = data['avatar']
        name     = data['name']
        content =  data['content']
        notificationId = data['notificationId']


        content = {
            'chatId' : chatId,
            'roomName':roomName,
            'author' :author,
            'avatar' :avatar,
            'name'   :name,
            'content':content,
            'notificationId': notificationId,
        }
        await self.channel_layer.group_send(self.room_group_name,
        {
            'type': 'notification_message',
            'message': content,
        })




    commands = {
    'notify_user': notify_user,
    }


    async def receive(self, text_data):

        data = json.loads(text_data)
        await self.commands[data['command']](self, data)



    async def notification_message(self, event):
        message = event['message']
        await self.send(text_data=json.dumps(message))
