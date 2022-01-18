from django.urls import path, include
#from magazine import urls
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import  *

app_name = 'social'

urlpatterns = [

path('notification/<int:notification_pk>/post/<int:post_pk>', PostNotification.as_view(), name="post-notification"),
path('notification/<int:notification_pk>/profile/<int:profile_pk>', FollowNotification.as_view(), name="follow-notification"),
path('notification/<int:notification_pk>/comment/<int:post_pk>/<int:comment_pk>', CommentNotification.as_view(), name="comment-notification"),
path('notification/<int:notification_pk>/comment_of_comment/<int:post_pk>/<int:comment_pk>/<int:com_of_com_pk>', ComOfComNotification.as_view(), name="com-of-com-notification"),
path('notification/<int:notification_pk>/remove_notification', remove_notification, name = 'remove-notification'),
path('notification/ajax', ajax_notifications, name = 'ajax-notifications'),
]
