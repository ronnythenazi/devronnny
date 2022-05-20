from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.models import Group, Permission
from magazine.models import Profile

def deactivate_user(username):
    user = User.objects.get(username = username)
    user.is_active = False
    user.save()

def activate_user(username):
    user = User.objects.get(username = username)
    user.is_active = True
    user.save()

def get_all_active_usernames_start_with(query_s):
    users_list = User.objects.filter(username__startswith = query_s).filter(is_active = True).values_list('username',flat=True).order_by('username')
    return list(users_list)

def get_all_active_users():
    users_list = User.objects.filter(is_active = True)
    return users_list

def get_all_active_usernames():
    users_list = User.objects.filter(is_active = True).values_list('username',flat=True).order_by('username')
    return list(users_list)

def get_all_active_usernames_unsorted():
    users_list = User.objects.filter(is_active = True).values_list('username',flat=True)
    return list(users_list)

def get_user(username):
    user = User.objects.get(username = username)
    return user

def get_profile(user):
    profile = Profile.objects.get(user = user)
    return profile

def is_username_exists(username):
    return User.objects.filter(username = username).exists()

def is_username_active(username):
    return User.objects.filter(is_active = True).filter(username = username).exists()

def get_active_profile_lst_start_with(s_query):
    users_list = get_all_active_usernames_start_with(s_query)
    filtered_usr_lst = get_profile_info_lst(users_list)
    return filtered_usr_lst

def get_active_profile_partial_lst_start_with(s_query, max_length = 20):
    #get_profile_lst_start_with
    users_list = get_all_active_usernames_start_with(s_query)[:max_length]
    filtered_usr_lst = get_profile_info_lst(users_list)
    return filtered_usr_lst

def get_profile_info_lst(users_list):
    profile_info_lst = []
    for username in users_list:
        user_info = get_profile_info_for_validated_user(username)
        profile_info_lst.append(user_info)
    return profile_info_lst



def filter_lst_to_active_users(lst, clear_prefix = '@'):
    filterd_lst = []
    for username in lst:
        username = username.replace(clear_prefix, '')
        if is_username_active(username) == False:
            continue
        filterd_lst.append(username)
    return filterd_lst


def get_profile_info_for_validated_user(username):
    user = get_user(username)
    profile = get_profile(user)
    info = {}
    info['username'] = str(username)
    info['avatar'] = str(profile.profile_img.url)
    return info

def get_profile_info(username):
    if is_username_exists(username) == False:
        return {}
    return get_profile_info_for_validated_user(username)
