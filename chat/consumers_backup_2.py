from django.contrib.auth import get_user_model
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json
from .models import Message, Chat
from users.models import Contact
from .views import (get_last_messages, get_user_contact, get_current_chat, get_or_create_private_chat_room
, save_message_for_chat
)
from users.members import get_profile_info_nick_or_user

#from channels.generic.websocket import AsyncWebsocketConsumer

User = get_user_model()


class ChatConsumer(WebsocketConsumer):

    def messages_to_json(self, messages):
        result = []

        for message in messages:

            result.append(self.message_to_json(message))
        return result



    def message_to_json(self, message):
        info = get_profile_info_nick_or_user(message.contact.user)
        avatar = info['avatar']
        name   = info['name']
        return {
            'id': str(message.id),
            'author': message.contact.user.username,
            'content': str(message.content),
            'timestamp': str(message.timestamp),
            'avatar'   : avatar,
            'name'     : name,
        }

    def fetch_messages(self, data):

        chat_id =  get_or_create_private_chat_room(data['from'], data['to'])

        messages = get_last_messages(chat_id)
        content = {
            'command': 'messages',
            'chatId' :  str(chat_id),
            'messages': self.messages_to_json(messages)
        }

        self.send_message(content)


    def new_message(self, data):
        user_contact =  get_user_contact(data['from'])
        current_chat = get_current_chat(data['chatId'])
        message = save_message_for_chat(current_chat, user_contact, data['message'])


        content = {
            'command': 'new_message',
            'message': self.message_to_json(message)
        }
        return self.send_chat_message(content)









    commands = {
        'fetch_messages': fetch_messages,
        'new_message': new_message,

    }




    def connect(self):

        self.room_name = self.scope['url_route']['kwargs']['room_name']

        self.room_group_name = f"chat_{self.room_name}"

        async_to_sync(self.channel_layer.group_add)(self.room_group_name,self.channel_name)

        self.accept()


    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(self.room_group_name,self.channel_name)


    def receive(self, text_data):

        data = json.loads(text_data)

        self.commands[data['command']](self, data)


    def send_chat_message(self, message):
        async_to_sync(self.channel_layer.group_send)(self.room_group_name,
        {
            'type': 'chat_message',
            'message': message
        }
    )



    def send_message(self, message):
        self.send(text_data=json.dumps(message))

    def chat_message(self, event):
        message = event['message']
        self.send(text_data=json.dumps(message))
