from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from magazine.models import Comment, Profile, BlogPost, comment_of_comment, Notification
from magazine.dates import get_total_diff_seconds, get_curr_datetime, get_curr_s_datetime

def get_post(notification_pk):
    notification_obj = Notification.objects.get(pk = notification_pk)
    if not notification_obj.comment == None:
        com = notification_obj.comment
        post = com.post
        return post
    if not notification_obj.com_of_com == None:
        sub_com = notification_obj.com_of_com
        com = notification_obj.com_of_com.comment
        post = com.post
        return post
    if not notification_obj.post == None:
        post = notification_obj.post
        return post

def follow_post_by_sending_com(com):
    usr = com.comment_usr
    post = com.post
    follow_post(post, usr)
    follow_com(com, usr)
    notify_all_followers(com, usr)

def follow_com_by_sending_sub_com(sub_com):
    com = sub_com.comment
    usr = sub_com.comment_of_comment_usr
    post = com.post
    follow_com(com, usr)
    follow_post(post, usr)
    notify_all_followers(sub_com, usr)
    print('notify_all_followers(sub_com, usr)')

def follow_post(post, follower):
    is_already_follow = post.followers.filter(id = follower.id).exists()
    if is_already_follow == False:
        post.followers.add(follower)

def follow_com(com, follower):
    is_already_follow = com.followers.filter(id = follower.id).exists()
    if is_already_follow == False:
        com.followers.add(follower)

def notify_all_followers(obj, notifyer):
    if isinstance(obj, comment_of_comment):
        com  = obj.comment
        post = com.post
        for follower in com.followers.all():
            is_usr_follow_post = post.followers.filter(id = follower.id).exists()
            if is_usr_follow_post:
                continue
            if is_notifyer_replied_to_follower(obj, follower):
                continue
            Notification.objects.create(notification_type = 6, from_user = notifyer, com_of_com = obj, to_user = follower)
        for follower in post.followers.all():
            if is_notifyer_replied_to_follower(obj, follower):
                continue
            Notification.objects.create(notification_type = 6, from_user = notifyer, com_of_com = obj, to_user = follower)

    elif isinstance(obj, Comment):
        post = obj.post
        for follower in post.followers.all():
            Notification.objects.create(notification_type = 5, from_user = notifyer, comment = obj, to_user = follower)

def is_notifyer_replied_to_follower(sub_com, follower):
    to_sub_com = sub_com.to_sub_comment
    if not to_sub_com == None:
        replied_to_who = to_sub_com.comment_of_comment_usr
        if replied_to_who == follower:
            return True
    else:
        com = sub_com.comment
        replied_to_who = com.comment_usr
        if replied_to_who == follower:
            return True
    return False
