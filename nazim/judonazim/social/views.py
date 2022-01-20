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


# Create your views here.


def ajax_notifications(request):
    if request.is_ajax and request.method == "GET":
        if(not request.user.is_authenticated):
            return JsonResponse({"error": "not logged in"}, status=400)

        request_user = request.user
        s_last_notification_date = str(request.GET.get("last_notification_date", None))
        if(s_last_notification_date == '0'):
            next_notifications = Notification.objects.filter(to_user = request_user).exclude(user_has_seen = True).order_by('-date')
            #ser_instance = serializers.serialize('json', list(next_notifications))#new

            from_users = Notification.objects.filter(to_user = request_user).exclude(user_has_seen = True).order_by('-date').values_list('from_user', flat=True)
            lst_next_notifications = list(next_notifications) #new
            if from_users:
                from_user = User.objects.get(id = from_users[0]) #new
                lst_next_notifications.append(from_user) #new

            ser_instance = serializers.serialize('json', lst_next_notifications) #new

            return JsonResponse({"next_notifications": ser_instance})
        #last_notification_date = parse_datetime(s_last_notification_date)
        #last_notification_date = datetime.fromisoformat(s_last_notification_date)
        #is_old_notification = Notification.objects.filter(to_user = request_user).filter(date = last_notification_date).exclude(user_has_seen = True).exists()
        #if(is_old_notification == False):

        try:
            print('try adding 999 at the end of datetime')
            last_notification_date = datetime.fromisoformat(s_last_notification_date + '999')
            print('new date is now' + str(last_notification_date))
        except:
            print('failed adding 999')
            last_notification_date = datetime.fromisoformat(s_last_notification_date)
            print('new date is now ' +  str(last_notification_date))
        print('local date pass as:' + s_last_notification_date)

        try:
            server_date_qs = Notification.objects.filter(to_user = request_user).exclude(user_has_seen = True).order_by('-date').values_list('date', flat = True)[0]
            server_date = str(server_date_qs)
            print('server date:', server_date)
        except:
            pass



        next_notifications = Notification.objects.filter(to_user = request_user).filter(date__gt = last_notification_date).exclude(user_has_seen = True).order_by('-date')#from user

        #new
        from_users = Notification.objects.filter(to_user = request_user).filter(date__gt = last_notification_date).exclude(user_has_seen = True).order_by('-date').values_list('from_user', flat=True)

        lst_next_notifications = list(next_notifications) #new
        if from_users:
            from_user = User.objects.get(id = from_users[0]) #new
            lst_next_notifications.append(from_user) #new

        ser_instance = serializers.serialize('json', list(lst_next_notifications)) #new

        #ser_instance = serializers.serialize('json', list(next_notifications))new
        return JsonResponse({"next_notifications": ser_instance})

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
