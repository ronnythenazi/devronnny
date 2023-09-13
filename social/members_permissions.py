from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from magazine.models import Comment, Profile, BlogPost, comment_of_comment, is_edit_date_expired
from .coms import get_com_author, get_com_created_date
from magazine.dates import get_total_diff_seconds, get_curr_datetime, get_curr_s_datetime
exposed_request = None

def f_is_user_admin():
    groups = list(exposed_request.user.groups.values_list('name',flat = True))
    if "admin" in groups:
        return True
    if "owner" in groups:
        return True
    return False

def f_is_user_owner():
    groups = list(exposed_request.user.groups.values_list('name',flat = True))
    if "owner" in groups:
        return True
    return False

def is_user_owner(user):
    groups = list(user.groups.values_list('name',flat = True))
    if "owner" in groups:
        return True
    return False

def f_is_user_author(com_type, com_id):
    author = get_com_author(com_type, com_id)
    if exposed_request.user == author:

        return True

    return False

def is_edit_period_over(com_date):
    return is_edit_date_expired(com_date)

def is_user_allowed_to_edit(com_type, com_id):
    if not exposed_request.user.is_authenticated:
        return {'answer':False, 'reason':'not authenticated'}
    is_user_owner = f_is_user_owner()
    is_user_author = f_is_user_author(com_type, com_id)
    if is_user_author == False and is_user_owner == False:
        return {'answer':False, 'reason':'not author'}
    com_date = get_com_created_date(com_type, com_id)
    is_user_admin = f_is_user_admin()
    if is_edit_period_over(com_date) and is_user_admin == False:
        return {'answer':False, 'reason':'time over'}
    if is_user_admin == False:
        return {'answer':True, 'show-date-edited':'true'}
    return {'answer':True, 'show-date-edited':'false'}
