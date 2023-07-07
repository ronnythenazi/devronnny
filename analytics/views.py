from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, Http404, redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.utils.dateparse import parse_datetime

from .visitors import (get_member_visitors_for_post,
get_anonymous_visitors_for_post, set_visitor_date_for_post, set_visitor_date,
get_member_visitors, get_anonymous_visitors)


def get_member_visitors_ajax(request):
    if not request.is_ajax or not request.method == "GET":
        return JsonResponse({'status':'not-ajax'})

    
    result = get_member_visitors()
    return JsonResponse(result, safe=False)

def get_anonymous_visitors_ajax(request):
    if not request.is_ajax or not request.method == "GET":
        return JsonResponse({'status':'not-ajax'})
    result = get_anonymous_visitors()
    return JsonResponse(result, safe=False)


def get_member_visitors_for_post_ajax(request):
    if request.is_ajax and request.method == "GET":
        page_id = request.GET.get('page_id')
        result = get_member_visitors_for_post(page_id)
        return JsonResponse(result, safe=False)






def get_anonymous_visitors_for_post_ajax(request):
    if request.is_ajax and request.method == "GET":
        page_id = request.GET.get('page_id')

        result = get_anonymous_visitors_for_post(page_id)

        return JsonResponse(result, safe=False)





def set_visitor_date_for_post_ajax(request):
    if not request.is_ajax or not request.method == "POST":
        return JsonResponse({'status':'not-ajax'})

    page_id = request.POST.get('page_id')
    set_visitor_date_for_post(request, page_id)

    return JsonResponse({'status':'succeeded'})


def set_visitor_date_for_homepage_ajax(request):
    if not request.is_ajax or not request.method == "POST":
        return JsonResponse({'status':'not-ajax'})

    set_visitor_date(request)

    return JsonResponse({'status':'succeeded'})
