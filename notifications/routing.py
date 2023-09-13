from django.urls import re_path

from . import sockets

websocket_urlpatterns = [
    re_path(r"ws/notifications/(?P<room_name>\w+)/$", sockets.notificationsSockets.as_asgi()),
    #re_path(r"ws/notifications/(?P<room_name>\w+)/$", notifications.ChatNotifications.as_asgi()),
    #re_path(r"ws/chat/(?P<room_name>[^/]+)/$", consumers.ChatConsumer),
]
