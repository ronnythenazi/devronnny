from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from magazine.models import Comment, Profile, BlogPost, comment_of_comment, Notification
from magazine.dates import get_total_diff_seconds, get_curr_datetime, get_curr_s_datetime
from django.urls import reverse

from django.utils.encoding import force_bytes, force_text, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from users.utils import token_generator
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives, send_mail
import threading
from .coms import get_article_obj, get_this_obj_type, get_com_author
from users.members import get_all_active_users, filter_lst_to_active_users
from general.regex import get_taged_users, replaceWordNotStartWithWord
exposed_request = None

def replaceTaggedUsersToTaggedElemesInCom(com):
    body = com.body
    s_body = str(body)
    lst_tagged_users = get_validated_tagged_users_from_txt(s_body)
    for username in lst_tagged_users:
        start_with = '@' + username
        s_body = getTaggedUserElemString(start_with, s_body)
    com.body = s_body
    com.save()

def getTaggedUserElemString(start_with, s):
    cname = 'tagged-user'
    not_start_with = 'class="' + cname + '">'
    replace_with = '<span class="' + cname + '">'+ start_with +'</span>'
    new_s_body = replaceWordNotStartWithWord(not_start_with, start_with, replace_with, s)
    return new_s_body

def isUserAlreadyTagged(start_with, s):
    new_s_body = getTaggedUserElemString(start_with, s)
    if s == new_s_body:
        return True
    return False

def get_validated_tagged_users_from_txt(s):
    tagged_strings = get_taged_users(s)
    filterd_lst = filter_lst_to_active_users(tagged_strings)
    return filterd_lst

def follow_or_unfollow(type, id, flag):
    obj = get_article_obj(type, id)
    login_user = exposed_request.user
    if flag == 'follow':
        follow_obj(obj, login_user)
        return
    unfollow_obj(obj, login_user)
    return


class EmailThread(threading.Thread):
    def __init__(self, email):
        self.EmailMultiAlternatives = email
        threading.Thread.__init__(self)

    def run(self):
        self.EmailMultiAlternatives.send(fail_silently=False)




def send_mail_notification(notification_pk):
    obj = get_notification_obj(notification_pk)
    to_user = obj.to_user
    from_user = obj.from_user
    notification_type = obj.notification_type
    post = get_post(notification_pk)
    title = post.title

    subject = 'message from judonazism'
    pos =  ""
    com_or_sub_com = ''
    respond_to_com = ''
    his_response = ''

    if not obj.comment == None:
        com  = obj.comment
        com_or_sub_com = 'com'
        pos = "-replace-me-comment" + str(com.pk)
    elif not obj.com_of_com == None:
        sub_com = obj.com_of_com
        com_or_sub_com = 'sub_com'
        pos = "-replace-me-sub-comment" + str(sub_com.pk)
    elif not obj.post == None:
        pos = ''
        com_or_sub_com = 'post'

    domain  = get_current_site(exposed_request).domain
    if pos == '':
        link = reverse('magazine:anArticle', args = [post.pk])
    else:
        link = reverse('magazine:anArticle', args = [post.pk, pos])

    url = 'http://' + domain + link

    template_name = "general/"
    if notification_type == 1 and com_or_sub_com == 'post':
        template_name += "like_your_post.html"
        respond_to_com = ''
        his_response = ''
    elif notification_type == 4 and com_or_sub_com == 'post':
        template_name += "dislike_your_post.html"
        respond_to_com = ''
        his_response = ''
    elif notification_type == 9 and com_or_sub_com == 'post':
        template_name += "new_post.html"
        respond_to_com = ''
        his_response = ''

    elif notification_type == 1 and com_or_sub_com == 'com':
        template_name += "like_your_com.html"
        respond_to_com = obj.comment.body
        his_response = ''
    elif notification_type == 2 and com_or_sub_com == 'com':
        template_name += "respond_your_post.html"
        respond_to_com = ''
        his_response = obj.comment.body
    elif notification_type == 4 and com_or_sub_com == 'com':
        template_name += "dislike_your_com.html"
        respond_to_com = obj.comment.body
        his_response = ''
    elif notification_type == 5 and com_or_sub_com == 'com':
        template_name += "respond_to_post_you_are_follow.html"
        respond_to_com = ''
        his_response = obj.comment.body

    elif notification_type == 1 and com_or_sub_com == 'sub_com':
        template_name += "like_your_com.html"
        respond_to_com = obj.com_of_com.body
        his_response = ''
    elif notification_type == 2 and com_or_sub_com == 'sub_com':
        template_name += "respond_to_you_under_com.html"
        respond_to_com = obj.com_of_com.comment.body
        his_response = obj.com_of_com.body

    elif notification_type == 4 and com_or_sub_com == 'sub_com':
        template_name += "dislike_your_com.html"
        respond_to_com = obj.com_of_com.body
        his_response = ''
    elif notification_type == 6 and com_or_sub_com == 'sub_com':
        template_name += "respond_under_com_you_are_follow.html"
        respond_to_com = obj.com_of_com.comment.body
        his_response = obj.com_of_com.body

    elif notification_type == 8:
        print('notification_type == 8 tag you mother fucker')
        template_name += "tag_you.html"
        respond_to_com = ''
        his_response = ''
    #body = 'Hello ' + usr.username + ' Please use this link to verify your account\n' + active_url
    txt_name = template_name.replace('html', 'txt')
    msg_htmly = get_template(template_name)
    msg_plaintext = get_template(txt_name)
    dict =  {'to_user':to_user, 'from_user':from_user,'post_title':title,'respond_to_com':respond_to_com,'his_response':his_response, 'link':url}
    text_content = msg_plaintext.render(dict)
    html_content = msg_htmly.render(dict)
    email = EmailMultiAlternatives(
        subject,
        html_content,
        #'noreply@semycolon.com',
        'notifications.ronnywasright.com',
        [to_user.email],
     )







    email.attach_alternative(html_content, "text/html")
    #email.send(fail_silently=True)
    EmailThread(email).start()


def get_notification_obj(notification_pk):
    notification_obj = Notification.objects.get(pk = notification_pk)
    return notification_obj


def get_notification_type(notification_pk):
    notification_obj = Notification.objects.get(pk = notification_pk)
    return notification_obj.notification_type


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

def unfollow_obj(obj, follower):
    print('try to unfollow obj')
    is_already_follow = obj.followers.filter(id = follower.id).exists()
    if is_already_follow == True:
        obj.followers.remove(follower)
        print('remove follower')

def follow_obj(obj, follower):
    is_already_follow = obj.followers.filter(id = follower.id).exists()
    if is_already_follow == False:
        obj.followers.add(follower)


def follow_post(post, follower):
    is_already_follow = post.followers.filter(id = follower.id).exists()
    if is_already_follow == False:
        post.followers.add(follower)

def follow_com(com, follower):
    is_already_follow = com.followers.filter(id = follower.id).exists()
    if is_already_follow == False:
        com.followers.add(follower)

def get_notification_obj_type_from_id(notification_pk):
    obj = get_notification_obj(notification_pk)
    type = get_notification_obj_type(obj)
    return type

def get_notification_obj_type(obj):
    type = ''
    if not obj.comment == None:
        type = 'com'
    elif not obj.com_of_com == None:
        type = 'sub_com'
    elif not obj.post == None:
        type = 'post'
    return type




def tag_user(com):
    body = com.body
    s_body = str(body)
    com_type = get_this_obj_type(com)
    author = get_com_author(com_type, com.id)
    if '@' not in s_body:
        return
    users = get_all_active_users()
    tagged_users = get_taged_users(s_body)
    for user in users:
        username = str(user.username)
        if isUserAlreadyTagged('@' + username, s_body):
            continue
        if ('@' + username) in tagged_users:
            notification = add_notification(8, author, user, com, com_type)
            send_mail_notification(notification.pk)

def notify_users_for_new_post(from_user, post):
    curr_user = from_user
    recipents = get_all_active_users()
    for recipent in recipents:
        notification = add_notification(9, from_user, recipent, post, 'post')
        send_mail_notification(notification.pk)

def add_notification(type, from_user, to, obj, obj_type = None):
    if obj_type == None:
        return None
    if obj_type == 'sub_com':
        notification = Notification.objects.create(notification_type = type, from_user = from_user, com_of_com = obj, to_user = to)
        return notification
    if obj_type == 'com':
        notification = Notification.objects.create(notification_type = type, from_user = from_user, comment = obj, to_user = to)
        return notification
    if obj_type == 'post':
        notification = Notification.objects.create(notification_type = type, from_user = from_user, post = obj, to_user = to)
        return notification
    return None




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
            notification = Notification.objects.create(notification_type = 6, from_user = notifyer, com_of_com = obj, to_user = follower)
            send_mail_notification(notification.pk)
        for follower in post.followers.all():
            if is_notifyer_replied_to_follower(obj, follower):
                continue
            notification = Notification.objects.create(notification_type = 6, from_user = notifyer, com_of_com = obj, to_user = follower)
            send_mail_notification(notification.pk)

    elif isinstance(obj, Comment):
        post = obj.post
        for follower in post.followers.all():
            notification = Notification.objects.create(notification_type = 5, from_user = notifyer, comment = obj, to_user = follower)
            send_mail_notification(notification.pk)

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
