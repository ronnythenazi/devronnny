from django.contrib.auth import get_user_model
from asgiref.sync import sync_to_async, async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json
from .models import Message, Chat
from users.models import Contact
from .views import (get_last_messages, get_user_contact, get_current_chat, get_or_create_private_chat_room
, save_message_for_chat, messages_to_json, message_to_json_called_from_async
)
from users.members import get_profile_info_nick_or_user

from channels.generic.websocket import AsyncWebsocketConsumer
import asyncio
import nest_asyncio
nest_asyncio.apply()

User = get_user_model()







class ChatConsumer(AsyncWebsocketConsumer):
    #loop = asyncio.new_event_loop()
    #asyncio.set_event_loop(loop)





    async def fetch_messages(self, data):

        chat_id =  await get_or_create_private_chat_room(data['from'], data['to'])

        messages = await get_last_messages(chat_id)




        content = {
            'command': 'messages',
            'chatId' :  str(chat_id),
            #'messages': asyncio.run(messages_to_json(messages))
            'messages': await messages_to_json(messages),
        }

        await self.send_message(content)


    async def new_message(self, data):
        user_contact =  await get_user_contact(data['from'])
        current_chat = await get_current_chat(data['chatId'])
        message = await save_message_for_chat(current_chat, user_contact, data['message'])


        content = {
            'command': 'new_message',
            'message': await message_to_json_called_from_async(message)
        }
        return await self.send_chat_message(content)









    commands = {
        'fetch_messages': fetch_messages,
        'new_message': new_message,

    }




    async def connect(self):

        self.room_name = self.scope['url_route']['kwargs']['room_name']

        self.room_group_name = f"chat_{self.room_name}"

        await self.channel_layer.group_add(self.room_group_name,self.channel_name)

        await self.accept()


    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name,self.channel_name)


    async def receive(self, text_data):

        data = json.loads(text_data)
        await self.commands[data['command']](self, data)



    async def send_chat_message(self, message):
        await self.channel_layer.group_send(self.room_group_name,
        {
            'type': 'chat_message',
            'message': message
        }
    )



    async def send_message(self, message):
        await self.send(text_data=json.dumps(message))


    async def chat_message(self, event):
        message = event['message']
        await self.send(text_data=json.dumps(message))
