from django.http import HttpResponse
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from .models import Comment, Profile, BlogPost, comment_of_comment
from django.utils.functional import wraps


def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if(not request.user.is_authenticated):
            return HttpResponse('אינך מורשה כניסה לדף זה')#return redirect('magazine:magazineNews')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func

def check_if_post_and_comment_accessible(view_func):
        @wraps(view_func)
        def inner(request, idpost, idcomment, *args, **kwargs):
            post = get_object_or_404(BlogPost, pk = idpost)
            comment = get_object_or_404(Comment, pk = idcomment)
            if(post is None or comment is None or post.publishstatus == 'private'):
                return HttpResponse('הדף שאתה מבקש אינו זמין')
            else:
                return view_func(request, idpost, idcomment, *args, **kwargs)
        return inner

def check_if_post_accessible(view_func):
        @wraps(view_func)
        def inner(request, pk, *args, **kwargs):
            post = get_object_or_404(BlogPost, pk = pk)
            if(post is None or post.publishstatus == 'private'):
                return HttpResponse('הדף שאתה מבקש אינו זמין')
            else:
                return view_func(request, pk, *args, **kwargs)
        return inner

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
