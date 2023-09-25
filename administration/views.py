from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, Http404, redirect
from django.urls import reverse
from django.http import JsonResponse
from django.utils.dateparse import parse_datetime
from users.members import get_profile_info_nick_or_user
from django.contrib.auth.models import User
#from django.db.models import Q
from .moderators import hideCom, unhideCom



def hideCommentAjax(request):
    if request.user.is_authenticated == False:
        return JsonResponse({'status':'not-log-in'})
    if not request.is_ajax or not request.method == "POST":
        return JsonResponse({'status':'not ajax get'})
    user = request.user
    objName = request.POST.get('comType')
    id      = request.POST.get('id')
    result = hideCom(objName, id, user)
    if result == False:
        return JsonResponse({'status':'access is denied'})
    return JsonResponse({'status':'success'})


def unhideCommentAjax(request):
    if request.user.is_authenticated == False:
        return JsonResponse({'status':'not-log-in'})
    if not request.is_ajax or not request.method == "POST":
        return JsonResponse({'status':'not ajax get'})
    user = request.user
    objName = request.POST.get('comType')
    id      = request.POST.get('id')
    result = unhideCom(objName, id, user)
    if result == False:
        return JsonResponse({'status':'access is denied'})
    return JsonResponse({'status':'success'})
