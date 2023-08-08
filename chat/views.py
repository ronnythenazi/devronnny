from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, Http404, redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.utils.dateparse import parse_datetime
from users.members import get_profile_info_nick_or_user
from django.contrib.auth.models import User
# Create your views here.



def get_private_chat_users_details(request):

    if request.user.is_authenticated == False:
        return JsonResponse([{'status':'not-log-in'}, {'status':'not-log-in'}], safe=False)

    #0 index for sender, 1 index for reviver
    people = []
    info = get_profile_info_nick_or_user(request.user)
    info.update({'status':'log-in'})
    people.append(info)
    if request.is_ajax and request.method == "GET":
        user_id = request.GET.get('to_user_id')
        user = User.objects.get(id = user_id)
        info = get_profile_info_nick_or_user(user)
        info.update({'status':'log-in'})
        people.append(info)


        return JsonResponse(people, safe=False)
