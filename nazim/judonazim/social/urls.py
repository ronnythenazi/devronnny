from django.urls import path, include
#from magazine import urls
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import  *

app_name = 'social'

urlpatterns = [

path('notification/post/<int:notification_pk>/<int:post_pk>', PostNotification.as_view(), name="post-notification"),
path('notification/profile/<int:notification_pk>/<int:profile_pk>', FollowNotification.as_view(), name="follow-notification"),
path('notification/comment/<int:notification_pk>/<int:post_pk>/<int:comment_pk>', CommentNotification.as_view(), name="comment-notification"),
path('notification/comment_of_comment/<int:notification_pk>/<int:post_pk>/<int:comment_pk>/<int:com_of_com_pk>', ComOfComNotification.as_view(), name="com-of-com-notification"),
path('notification/remove_notification/<int:notification_pk>', remove_notification, name = 'remove-notification'),
path('notification/ajax', ajax_notifications, name = 'ajax-notifications'),
path('notification/ajax/comment', ajax_notification_comment, name = 'ajax_notification_comment'),
path('notification/ajax/comment-of-comment', ajax_notification_com_of_com, name = 'ajax_notification_com_of_com'),
path('notification/ajax/from-user', ajax_get_user_name, name = 'ajax_get_user_name'),
path('post-rating-save-update/rate_post_save_ajax', rate_post_save_ajax, name = "rate_post_save_ajax"),
path('post-rating-refresh/rate_post_refresh_ajax', rate_post_refresh_ajax, name = "rate_post_refresh_ajax"),
path('rate_com_save_ajax/', rate_com_save_ajax, name='rate_com_save_ajax'),
path('rate_com_refresh_ajax/', rate_com_refresh_ajax, name='rate_com_refresh_ajax'),
path('rate_sub_com_save_ajax/', rate_sub_com_save_ajax, name='rate_sub_com_save_ajax'),
path('rate_sub_com_refresh_ajax/', rate_sub_com_refresh_ajax, name='rate_sub_com_refresh_ajax'),
path('sub-com-save-ajax/', sub_com_save_ajax, name='sub-com-save'),
path('com-to-delete/', com_delete, name='com-delete'),
path('com-update/', com_update, name='com-update'),
path('notification/follow-com-notification/<int:notification_pk>', follow_com_notification, name='follow-com-notification'),
path('notification/follow-sub-com-notification/<int:notification_pk>', follow_sub_com_notification, name='follow-sub-com-notification'),
path('notification/get-post', get_post_ajax, name = 'get-post'),
path('notification/page-404', page_not_found, name='page-404'),

]
