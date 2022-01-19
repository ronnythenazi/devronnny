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



# Create your views here.


def ajax_notifications(request):
    # request should be ajax and method should be POST.

    if request.is_ajax and request.method == "GET":
        #notifications = Notification.objects.filter(to_user = request_user).exclude(user_has_seen = True).order_by('-date')
        request_user = request.user
        s_last_notification_date = str(request.GET.get("last_notification_date", None))

        if(s_last_notification_date == '0'):
            next_notifications = Notification.objects.filter(to_user = request_user).exclude(user_has_seen = True).order_by('-date')
            ser_instance = serializers.serialize('json', list(next_notifications))

            return JsonResponse({"next_notifications": ser_instance})

        last_notification_date = datetime.fromisoformat(s_last_notification_date)
        is_old_notification = Notification.objects.filter(to_user = request_user).filter(date = last_notification_date).exclude(user_has_seen = True).exists()
        if(is_old_notification == False):
            s_last_notification_date += '999'
        last_notification_date = datetime.fromisoformat(s_last_notification_date)
        print('local date pass as:' + s_last_notification_date)
        next_notifications = Notification.objects.filter(to_user = request_user).filter(date__gt = last_notification_date).exclude(user_has_seen = True).order_by('-date')

        #server_date = Notification.objects.filter(to_user = request_user).filter(date__gt = last_notification_date).exclude(user_has_seen = True).order_by('-date').values_list('date', flat = True)[0]


        #print('server_date:' + str(server_date))
        #print('local date:' + str(last_notification_date))


        ser_instance = serializers.serialize('json', list(next_notifications))

        return JsonResponse({"next_notifications": ser_instance})


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
