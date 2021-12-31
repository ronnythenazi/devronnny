from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from .models import Comment, Profile


def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if(not request.user.is_authenticated):
            return HttpResponse('אינך מורשה כניסה לדף זה')#return redirect('magazine:magazineNews')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func




def allowed_users(allowed_roles = []):
    def deocrator(view_func):
        def wrapper_func(request, *args, **kargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_roles:
                return view_func(request, *args, **kargs)
            else:
                return HttpResponse('אינך מורשה כניסה לדף זה')

        return wrapper_func
    return deocrator

def add_def_group_if_not_exist(def_group = 'members'):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            new_group, created = Group.objects.get_or_create(name=def_group)
            return view_func(request, *args, **kwargs)

        return wrapper_func
    return decorator
