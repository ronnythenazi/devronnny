from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, Http404, redirect
from magazine.models import BlogPost, Profile, Comment, Notification, comment_of_comment
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from django.forms import modelformset_factory
from django.db.models import Count, Q
from django.utils.dateparse import parse_datetime
from datetime import datetime, timedelta
from django.views import View
import math
from django.http import JsonResponse
from django.core import serializers
from django.utils.dateparse import parse_datetime
from django.utils import timezone
import dateutil.parser
from datetime import datetime
from django.contrib.auth.models import User
from .calcs import get_total_seconds

def sub_com_save_ajax(request):
    if request.method == 'POST' and request.is_ajax:
        com_parent_id = request.POST.get('com_parent_id')
        print('sub_com_save_ajax:com_parent_id=' + str(com_parent_id))
        com_parent = get_object_or_404(Comment, id = com_parent_id)
        replied_to_sub_com_id = request.POST.get('replied_to_sub_com_id')
        print('sub_com_save_ajax:replied_to_sub_com_id=' + str(replied_to_sub_com_id))
        body = request.POST.get('body')
        #print('sub_com_save_ajax:body=' + str(body))
        if replied_to_sub_com_id == None or replied_to_sub_com_id == '':
            if request.user.is_authenticated:
                sub_com = comment_of_comment.objects.create(comment_of_comment_usr = request.user, body = body, comment = com_parent)
                notification = Notification.objects.create(notification_type = 2, from_user = request.user, com_of_com = sub_com, to_user = com_parent.comment_usr)
                print('sub_com_save_ajax:saved comment to user ' + str(request.user.username))
            else:
                sub_com = comment_of_comment.objects.create(body = body, comment = com_parent)
                notification = Notification.objects.create(notification_type = 2,  com_of_com = sub_com, to_user = com_parent.comment_usr)
                print('sub_com_save_ajax:saved comment to someone')
        else:
            replied_to_sub_com = get_object_or_404(comment_of_comment, id = replied_to_sub_com_id)
            print('replied_to_sub_com =' + str(replied_to_sub_com.id))
            if request.user.is_authenticated:
                sub_com = comment_of_comment.objects.create(comment_of_comment_usr = request.user, body = body, comment = com_parent)
                print('new sub comment created')
                print('try sub_com.to_sub_comment = replied_to_sub_com')
                sub_com.to_sub_comment = replied_to_sub_com
                sub_com.save()
                print('success!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
                notification = Notification.objects.create(notification_type = 2, from_user = request.user, com_of_com = sub_com, to_user = com_parent.comment_usr)
                print('sub_com_save_ajax:saved replied to sub_com_id {sub_com_id} to user {user}'.format(sub_com_id = replied_to_sub_com_id, user = str(request.user.username)))
            else:
                sub_com = comment_of_comment.objects.create(body = body, comment = com_parent)
                sub_com.to_sub_comment = replied_to_sub_com
                sub_com.save()
                print('sub-com saved')
                notification = Notification.objects.create(notification_type = 2,  com_of_com = sub_com, to_user = com_parent.comment_usr)
                print('sub_com_save_ajax:saved replied to sub_com_id {sub_com_id} to someone'.format(sub_com_id = replied_to_sub_com_id))
        t = str(sub_com.date_added.strftime('%H:%M:%S'))
        print('sub_com_save_ajax: time =' + t)
        date = str(sub_com.date_added.strftime('%d/%m/%Y'))
        print('sub_com_save_ajax: date =' + date)
        return JsonResponse({'sub_com_id':str(sub_com.id), 'date':date, 'time':t})

def rate_sub_com_save_ajax(request):
    if not request.user.is_authenticated:
        return JsonResponse({})
    if request.method == 'POST' and request.is_ajax:
        com_of_com_pk = request.POST.get('com_of_com_pk')
        print('save_ajax:com_of_com_pk=' + str(com_of_com_pk))
        com_of_com = get_object_or_404(comment_of_comment, id = com_of_com_pk)
        rate_type = request.POST.get('rate_type')
        print('com_of_com-rate-type:' + rate_type)
        if rate_type == 'like-com-of-com':
            print('com_of_com liked')
            is_already_liked = com_of_com.likes.filter(id = request.user.id).exists()
            if is_already_liked:
                com_of_com.likes.remove(request.user)
                print('remove like for com_of_com')
            else:
                com_of_com.likes.add(request.user)
                com_of_com.dislikes.remove(request.user)
                notification = Notification.objects.create(notification_type = 1, from_user = request.user, com_of_com = com_of_com, to_user = com_of_com.comment_of_comment_usr)
                print('added like for com_of_com')
        elif rate_type == 'dislike-com-of-com':
            is_already_disliked = com_of_com.dislikes.filter(id = request.user.id).exists()
            if is_already_disliked:
                com_of_com.dislikes.remove(request.user)
                print('removed dislike for com_of_com')
            else:
                com_of_com.dislikes.add(request.user)
                com_of_com.likes.remove(request.user)
                notification = Notification.objects.create(notification_type = 4, from_user = request.user, com_of_com = com_of_com, to_user = com_of_com.comment_of_comment_usr)
                print('added dislike for com_of_com')
    return JsonResponse({})

def rate_post_refresh_ajax(request):
    if request.method == 'GET' and request.is_ajax:
        post_pk = request.GET.get('post_pk')
        #print('post_pk=' + str(post_pk))
        post = BlogPost.objects.get(pk = post_pk)
        rate_users = []
        for like in post.likes.all():
            rate_users.append({'user':str(like), 'rate-type': 'like'})
            #print('like-user:' + str(like))
        for dislike in post.dislikes.all():
            rate_users.append({'user':str(dislike), 'rate-type': 'dislike'})
        return JsonResponse(rate_users, safe = False)

def rate_sub_com_refresh_ajax(request):
    if request.method == 'GET' and request.is_ajax:
        post_pk = request.GET.get('post_pk')
        print('post_pk for rate_sub_com_refresh_ajax=' + str(post_pk))
        post = BlogPost.objects.get(pk = post_pk)
        sub_coms_rates = []
        for com in post.comments.all():
            for sub_com in com.comments_of_comment.all():
                rate_users = []
                for like in sub_com.likes.all():
                    rate_users.append({'user':str(like), 'rate-type': 'like'})
                    print('like-user: rate_com_refresh_ajax' + str(like))
                for dislike in sub_com.dislikes.all():
                    rate_users.append({'user':str(dislike), 'rate-type': 'dislike'})
                sub_com_rates_dict  = {'sub_com_pk':str(sub_com.pk), 'items':rate_users}
                sub_coms_rates.append(sub_com_rates_dict)

        return JsonResponse(sub_coms_rates, safe = False)

def rate_com_refresh_ajax(request):
    if request.method == 'GET' and request.is_ajax:
        post_pk = request.GET.get('post_pk')
        #print('post_pk for rate_com_refresh_ajax=' + str(post_pk))
        post = BlogPost.objects.get(pk = post_pk)
        coms_rates = []
        for com in post.comments.all():
            rate_users = []
            for like in com.likes.all():
                rate_users.append({'user':str(like), 'rate-type': 'like'})
                #print('like-user: rate_com_refresh_ajax' + str(like))
            for dislike in com.dislikes.all():
                rate_users.append({'user':str(dislike), 'rate-type': 'dislike'})
            com_rates_dict  = {'com_pk':str(com.pk), 'items':rate_users}
            coms_rates.append(com_rates_dict)
        return JsonResponse(coms_rates, safe = False)

def rate_com_save_ajax(request):
    if not request.user.is_authenticated:
        return JsonResponse({})
    if request.method == 'POST' and request.is_ajax:
        com_pk = request.POST.get('com_pk')
        #print('save_ajax:com_pk=' + str(com_pk))
        com = get_object_or_404(Comment, id = com_pk)
        rate_type = request.POST.get('rate_type')
        #print('rate-type:' + rate_type)
        if rate_type == 'like-com':
            #print('liked')
            is_already_liked = com.likes.filter(id = request.user.id).exists()
            if is_already_liked:
                #print('remove like')
                com.likes.remove(request.user)
            else:
                #print('added like')
                com.likes.add(request.user)
                com.dislikes.remove(request.user)
                notification = Notification.objects.create(notification_type = 1, from_user = request.user, comment = com, to_user = com.comment_usr)

        elif rate_type == 'dislike-com':
            is_already_disliked = com.dislikes.filter(id = request.user.id).exists()
            if is_already_disliked:
                com.dislikes.remove(request.user)
            else:
                com.dislikes.add(request.user)
                com.likes.remove(request.user)
                notification = Notification.objects.create(notification_type = 4, from_user = request.user, comment = com, to_user = com.comment_usr)
    return JsonResponse({})

def rate_post_save_ajax(request):
    if not request.user.is_authenticated:
        return JsonResponse({})
    if request.method == 'POST' and request.is_ajax:
        post_pk = request.POST.get('post_pk')
        #print('save_ajax:post_pk=' + str(post_pk))
        post = get_object_or_404(BlogPost, id = post_pk)
        rate_type = request.POST.get('rate_type')
        #print('rate-type:' + rate_type)
        if rate_type == 'like-btn':
            #print('liked')
            is_already_liked = post.likes.filter(id = request.user.id).exists()
            if is_already_liked:
                #print('remove like')
                post.likes.remove(request.user)
            else:
                #print('added like')
                post.likes.add(request.user)
                post.dislikes.remove(request.user)
                notification = Notification.objects.create(notification_type = 1, from_user = request.user, post = post, to_user = post.author)

        elif rate_type == 'dislike-btn':
            is_already_disliked = post.dislikes.filter(id = request.user.id).exists()
            if is_already_disliked:
                post.dislikes.remove(request.user)
            else:
                post.dislikes.add(request.user)
                post.likes.remove(request.user)
                notification = Notification.objects.create(notification_type = 4, from_user = request.user, post = post, to_user = post.author)
    return JsonResponse({})


def ajax_notifications(request):
    if request.is_ajax and request.method == "GET":
        if(not request.user.is_authenticated):
            return JsonResponse({"error": "not logged in"}, status=400)
        s_last_notification_date = str(request.GET.get("last_notification_date", None))
        if(s_last_notification_date == '0'):
            next_notifications = Notification.objects.filter(to_user = request.user.id).exclude(user_has_seen = True).order_by('-date')

            from_users = Notification.objects.filter(to_user = request.user.id).exclude(user_has_seen = True).order_by('-date').values_list('from_user', flat=True)
            lst_next_notifications = list(next_notifications) #new
            if from_users:
                from_user = User.objects.get(id = from_users[0]) #new
                lst_next_notifications.append(from_user) #new

            ser_instance = serializers.serialize('json', lst_next_notifications) #new

            return JsonResponse({"next_notifications": ser_instance})

        """
        try:
            print('try adding 999 at the end of datetime')
            last_notification_date = parse_datetime(s_last_notification_date + '999')
            print('new date is now' + str(last_notification_date))
        except:
            print('failed adding 999')
            last_notification_date = parse_datetime(s_last_notification_date)
            print('new date is now ' +  str(last_notification_date))
        print('local date pass as:' + s_last_notification_date)
        """
        last_notification_date = parse_datetime(s_last_notification_date)
        print('new date is now' + str(last_notification_date))
        print('local date pass as:' + s_last_notification_date)

        try:
            server_date = Notification.objects.filter(to_user = request.user.id).exclude(user_has_seen = True).order_by('-date').values_list('date', flat = True)[0]
            s_server_date = str(server_date)
            print('server date:', s_server_date)
            gap = get_total_seconds(server_date, last_notification_date)
            print('seconds diff=' + str(gap))
            if(gap < 0.5):
                return JsonResponse({"error": ""}, status=400)

        except Exception as ex:
            print(ex)
        lst_next_notifications = []
        next_notifications = Notification.objects.filter(to_user = request.user.id).filter(date__gt = last_notification_date).exclude(user_has_seen = True).order_by('-date')

        #from_users = Notification.objects.filter(to_user = request.user.id).exclude(user_has_seen = True).order_by('-date').values_list('from_user', flat=True)

        lst_next_notifications = list(next_notifications) #new
        #from_user = User.objects.get(id = from_users[0]) #new

        #lst_next_notifications.append(from_user) #new
        #print(from_user.username)

        ser_instance = serializers.serialize('json', lst_next_notifications) #new

        return JsonResponse({"next_notifications": ser_instance})



def ajax_get_user_name(request):
    print('ajax_get_user_name')
    notification_pk  = request.GET.get('notification_pk')
    user_id = Notification.objects.filter(pk = notification_pk)[0].from_user.id
    user = User.objects.filter(pk = user_id)
    ser_instance = serializers.serialize('json', list(user))
    print(user[0].username)
    return JsonResponse({'username':ser_instance})



def ajax_notification_comment(request):
    if request.is_ajax and request.method == "GET":
        if(not request.user.is_authenticated):
            return JsonResponse({"error": "not logged in"}, status=400)
        request_user = request.user
        comment_id = str(request.GET.get("comment_id", None))
        comment = Comment.objects.filter(id = comment_id)
        ser_instance = serializers.serialize('json', list(comment))
        return JsonResponse({"comment": ser_instance})

def ajax_notification_com_of_com(request):
    if request.is_ajax and request.method == "GET":
        if(not request.user.is_authenticated):
            return JsonResponse({"error": "not logged in"}, status=400)
        request_user = request.user
        com_of_com_id = str(request.GET.get("com_of_com_id", None))
        com_of_com = comment_of_comment.objects.filter(id = com_of_com_id)
        ser_instance = serializers.serialize('json', list(com_of_com))
        return JsonResponse({"com_of_com": ser_instance})

def remove_notification(request, notification_pk):
    notification = Notification.objects.get(pk = notification_pk)
    notification.delete()
    prev_page = request.GET.get('prev_page', '')
    print('prev_page=' + str(prev_page))
    #return redirect(prev_page)
    #return HttpResponseRedirect(prev_page)
    return HttpResponseRedirect(prev_page)

class PostNotification(View):
    def get(self, request, notification_pk, post_pk, *args, **kwargs):
        notification = Notification.objects.get(pk = notification_pk)
        post = BlogPost.objects.get(pk = post_pk)

        notification.user_has_seen = True
        notification.save()

        return redirect('magazine:anArticle', pk = post_pk)

class ComOfComNotification(View):
    def get(self, request, notification_pk, post_pk, comment_pk, com_of_com_pk, *args, **kwargs):
        notification = Notification.objects.get(pk = notification_pk)
        comment =  Comment.objects.get(pk = comment_pk)
        com_of_com =  comment_of_comment.objects.get(pk = com_of_com_pk)
        post = BlogPost.objects.get(pk = post_pk)

        notification.user_has_seen = True
        notification.save()

        return redirect('magazine:anArticle', pk = post_pk, pos_id = "-replace-me-sub-comment" + str(com_of_com_pk))

class CommentNotification(View):
    def get(self, request, notification_pk, post_pk, comment_pk, *args, **kwargs):
        notification = Notification.objects.get(pk = notification_pk)
        comment =  Comment.objects.get(pk = comment_pk)
        post = BlogPost.objects.get(pk = post_pk)

        notification.user_has_seen = True
        notification.save()

        return redirect('magazine:anArticle', pk = post_pk, pos_id = "-replace-me-comment" + str(comment_pk))


class FollowNotification(View):
    def get(self, request, notification_pk, profile_pk, *args, **kwargs):
        notification = Notification.objects.get(pk = notification_pk)
        profile = Profile.objects.get(pk = profile_pk)

        notification.user_has_seen = True
        notification.save()

        return redirect('magazine:magazineNews')
