from channels.generic.websocket import WebsocketConsumer
import json
from asgiref.sync import sync_to_async, async_to_sync
from users.members import get_profile_info_nick_or_user
from channels.generic.websocket import AsyncWebsocketConsumer
import asyncio
import nest_asyncio
nest_asyncio.apply()


from .notifications import (notifications_to_json, notification_to_json_called_from_async,
get_last_notifications,isAuthenticatedForNotifyForNotification,
)
#from .utils import send_chat_webpush_notification_called_from_async

class notificationsSockets(AsyncWebsocketConsumer):

    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f"notifications_{self.room_name}"
        await self.channel_layer.group_add(self.room_group_name,self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name,self.channel_name)





    async def new_notification(self, data):


        username =  self.scope["user"].username
        notificationId = data['notificationId']


        content = {
            'command': 'newNotification',
            'notification': await notification_to_json_called_from_async(notificationId, username),
        }
        return await self.send_notification_message(content)



    async def send_notification_message(self, notification):
        await self.send(text_data=json.dumps(notification))






    async def notificationOfNotification(self, data):
        username =  self.scope["user"].username
        notificationId = data['notificationId']
        isAuthenticated = await isAuthenticatedForNotifyForNotification(notificationId, username)
        if(isAuthenticated == False):
            return
            
        content = {
            'command': 'NotifyforNotification',
            'notificationId': str(notificationId),
        }
        return await self.notifyForNotificationHandler(content)


    async def notifyForNotificationHandler(self, message):
        await self.channel_layer.group_send(self.room_group_name,
        {
            'type': 'sendNotifiyOfNotification',
            'message': message,
        }
    )


    async def sendNotifiyOfNotification(self, event):
        message = event['message']
        await self.send(text_data=json.dumps(message))








    async def fetch_notifications(self, data):


        username =  self.scope["user"].username
        notifications = await get_last_notifications(username)


        content = {
            'command': 'fetchNotifications',
            'notifications': await notifications_to_json(notifications),
        }

        await self.send_notifications(content)


    async def send_notifications(self, notification):
        await self.send(text_data=json.dumps(notification))





    commands = {
    'newNotification': new_notification,
    'fetchNotifications':fetch_notifications,
    'NotifyforNotification'  :notificationOfNotification,
    }




    async def receive(self, text_data):
        data = json.loads(text_data)
        await self.commands[data['command']](self, data)
