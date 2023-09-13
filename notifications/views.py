from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, Http404, redirect
from django.urls import reverse
from django.http import HttpResponse, JsonResponse
from magazine.models import Notification
from .notifications import getNotificationPredcesorsUris
from users.members import get_profile_from_user_id
# Create your views here.







    #request.build_absolute_uri(reverse('magazine:anArticle', args = [post.pk, pos]))

def getClickedNotificationObjectUriAjax(request):
    if request.user.is_authenticated == False:
        return JsonResponse({'status':'not-log-in'})
    if not request.is_ajax or not request.method == "GET":
        return JsonResponse({'status':'not ajax get'})

    notificationId = request.GET.get('notificationId')
    urlType = request.GET.get('urlType')

    notification = Notification.objects.get(id = notificationId)
    to_user = notification.to_user
    current_user = request.user
    if(to_user.username != current_user.username):
        return JsonResponse({'status':'access is denied'})


    if(urlType == 'author'):
        profile = get_profile_from_user_id(notification.from_user.id)
        profile_url = request.build_absolute_uri(reverse('users:public-profile', args = [str(profile.id)]))
        return JsonResponse({'url':str(profile_url)})

    uris = getNotificationPredcesorsUris(notification)

    if(urlType == 'content'):
        uriContent = uris['content_reverse_url']
        content_url = request.build_absolute_uri(reverse(uriContent['viewName'], args = uriContent['args']))
        return JsonResponse({'url':str(content_url)})

    if(urlType == 'thumb'):
        uriThumb   = uris['thumb_reverse_url']
        thumb_url   = request.build_absolute_uri(reverse(uriThumb['viewName'], args = uriThumb['args']))
        return JsonResponse({'url':str(thumb_url)})
