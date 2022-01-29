from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from magazine.models import Comment, Profile, BlogPost, comment_of_comment
from magazine.dates import get_total_diff_seconds, get_curr_datetime, get_curr_s_datetime

def get_com(com_type, com_id):
    com = None
    if com_type == 'com':
        com = get_object_or_404(Comment, id = com_id)
    elif com_type == 'sub_com':
        com = get_object_or_404(comment_of_comment, id = com_id)
    return com

def get_com_author(com_type, com_id):
    com = get_com(com_type, com_id)
    if com_type == 'com':
        return com.comment_usr
        print('com.comment_usr\author -' + str(com.comment_usr))
    elif com_type == 'sub_com':
        return com.comment_of_comment_usr
    return None

def get_com_created_date(com_type, com_id):
    com = get_com(com_type, com_id)
    return com.date_added

def get_all_nested_coms_id(com, lst = []):
    for sub_com in com.replied_to.all():
        lst.append(sub_com.id)
        lst = get_all_nested_coms_id(sub_com, lst)
    return lst
