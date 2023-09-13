from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from magazine.models import Comment, Profile, BlogPost, comment_of_comment
from magazine.dates import get_total_diff_seconds, get_curr_datetime, get_curr_s_datetime


def get_article_obj(type, id):
    if type == 'post':
        post = get_object_or_404(BlogPost, id = id)
        return post
    return get_com(type, id)

def get_com(com_type, com_id):
    com = None
    if com_type == 'com':
        com = get_object_or_404(Comment, id = com_id)
    elif com_type == 'sub_com':
        com = get_object_or_404(comment_of_comment, id = com_id)
    return com
#for a notification obj
def get_obj_type(obj):
    type = ''
    if not obj.comment == None:
        type = 'com'
    elif not obj.com_of_com == None:
        type = 'sub_com'
    elif not obj.post == None:
        type = 'post'
    return type

def type_name_to_formal_model_type_name(type_name):
    if type_name == 'com':
        return 'Comment'
    if type_name == 'sub_com':
        return 'comment_of_comment'

def get_this_obj_type(obj):
    type = ''
    if isinstance(obj, comment_of_comment):
        return 'sub_com'
    if isinstance(obj, Comment):
        return 'com'


def get_obj_author(obj):
    com_type = get_this_obj_type(obj)
    id = obj.id
    author = get_com_author(com_type, id)
    return author

def get_post_author(post_id):
    post = get_object_or_404(BlogPost, id = post_id)
    return post.author

def get_com_author(com_type, com_id):
    com = get_com(com_type, com_id)
    if com_type == 'com':
        return com.comment_usr
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
