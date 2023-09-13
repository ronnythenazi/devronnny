from django.urls import path, include

from .views import (getClickedNotificationObjectUriAjax,)

app_name = 'notifications'


urlpatterns = [


path('getNotificationObjectUrl', getClickedNotificationObjectUriAjax, name="get-clicked-notification-obj-uri"),



]
