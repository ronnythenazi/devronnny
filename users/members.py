from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.models import Group, Permission
from magazine.models import Profile
from general.time import get_years_passed

from analytics.models import UserSession
from asgiref.sync import sync_to_async
from .models import UserTokenKey, UserTokenPublicKey

def check_if_user_online(username):
    is_online = UserSession.objects.filter(user__username=username).exists()
    if(is_online == True):
        return 'online'
    return 'offline'



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

def get_profile_from_profile_id(id):
    profile = get_object_or_404(Profile, id = id)
    return profile

def get_profile_from_user_id(id):
    profile = Profile.objects.get(user__id = id)
    return profile

def get_profile_from_username(username):
    profile = Profile.objects.get(user__username = username)
    return profile

def get_profile_snippet(username):
    profile = get_profile_from_username(username)
    user = User.objects.get(username = username)
    dict = {}
    dict['sex'] = str(profile.sex)
    dict['age'] = str(get_years_passed(profile.birthDate))

    if not profile.nick is None:
        dict['name'] = str(profile.nick)
    else:
        dict['name'] = str(user.username)
    dict['avatar'] = str(profile.profile_img.url)

    dict['profile_id'] = str(profile.id)

    return dict

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


def get_profile_info_nick_or_user(user):
    profile = get_profile(user)
    info = {}

    if not profile.nick is None:
        info['name'] = profile.nick
    else:
        info['name'] = str(user.username)
    info['avatar'] = str(profile.profile_img.url)
    return info

def get_profile_info(username):
    if is_username_exists(username) == False:
        return {}
    return get_profile_info_for_validated_user(username)


def get_user_token_key(username):
    user = User.objects.get(username = username)
    isTokenExist = UserTokenKey.objects.filter(user = user).exists()
    if(isTokenExist == False):
        password = User.objects.make_random_password(length=14, allowed_chars="abcdefghjkmnpqrstuvwxyz01234567889")
        UserTokenKey.objects.create(user = user, token = password)
        return password
    token = UserTokenKey.objects.get(user = user).token
    return token


def get_user_public_token_key(username):
    user = User.objects.get(username = username)
    isTokenExist = UserTokenPublicKey.objects.filter(user = user).exists()
    if(isTokenExist == False):
        password = User.objects.make_random_password(length=14, allowed_chars="abcdefghjkmnpqrstuvwxyz01234567889")
        UserTokenPublicKey.objects.create(user = user, token = password)
        return password
    token = UserTokenPublicKey.objects.get(user = user).token
    return token
