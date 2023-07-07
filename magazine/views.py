from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, Http404, redirect
from django.views.generic import ListView, DetailView , CreateView
from .models import BlogPost, Profile, Comment, Notification, comment_of_comment, Labels
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .blogpublishing import *
from django.forms import modelformset_factory
from .decorations import unauthenticated_user, allowed_users, check_if_post_accessible, check_if_post_and_comment_accessible
from django.db.models import Count, Q
from django.utils.dateparse import parse_datetime
from datetime import datetime, timedelta
from .dates import *
from social.notifications import (follow_post_by_sending_com,
tag_user, replaceTaggedUsersToTaggedElemesInCom, notify_users_for_new_post)

from users.members import activate_user, deactivate_user
from social.members_permissions import f_is_user_owner
from .articles import get_search_result, get_seach_result_qs_in_lst
from social.coms import get_post_author
from .posts import get_post_labels, update_post_labels, create_new_label_for_post
from .posts import update_label_name, remove_label
from .signals import user_visit_site



import math

def load_more_matched_articles_ajax(request):
    if not request.is_ajax or not request.method == "GET":
        return JsonResponse({})
    search = request.GET.get('search')
    from_post = request.GET.get('num_of_posts_loaded')
    search_results = get_search_result(search, start_from=int(from_post), max_per_page=10)
    lst = get_seach_result_qs_in_lst(search_results)
    return JsonResponse(lst, safe=False)

#@ensure_csrf_cookie
def search_articles(request):
    search = request.GET.get('search')
    search_results = get_search_result(search)
    context = {'posts': search_results, 'search':search}
    return render(request, 'magazine/posts_search_result.html', context)

def activate_user_ajax(request):
    if not request.is_ajax or not request.method == "POST":
        return JsonResponse({})
    if not request.user.is_authenticated:
        return JsonResponse({})
    username = request.POST.get('username')
    if f_is_user_owner() == False:
        return JsonResponse({})
    activate_user(username)
    return JsonResponse({})


def deactivate_user_ajax(request):
    if not request.is_ajax or not request.method == "POST":
        return JsonResponse({})
    if not request.user.is_authenticated:
        return JsonResponse({})
    username = request.POST.get('username')
    if f_is_user_owner() == False:
        return JsonResponse({})
    deactivate_user(username)
    return JsonResponse({})

@unauthenticated_user
@allowed_users(allowed_roles = ['owner'])
def manageUsersPermission(request):
    template = "magazine/permissions.html"

    if request.method == 'POST':
        frm = UsrToGroupForm(request.POST)
        if frm.is_valid():
            selected_group = frm.cleaned_data['group']
            groups = Group.objects.all()
            profiles = [Profile.objects.get(pk=pk) for pk in request.POST.getlist("members", "")]
            for prof in profiles:
                user = prof.user
                for group in groups:
                    if not (selected_group == group):
                        user.groups.remove(group)
                    elif not user.groups.filter(id = selected_group.id).count():
                        user.groups.add(selected_group)
                """
                if user.groups.filter(id = selected_group.id).count():
                    user.groups.remove(selected_group)
                else:
                    user.groups.add(selected_group)
                """
            return redirect('magazine:magazineNews')
    frm = UsrToGroupForm()
    return render(request, template, {'form':frm})


def about_ronny_the_nazi(request):
    return render(request, 'index.html', {'txtfilename' : 'mywebsitedevelopment.html'})


def f_allPosts_next(request, s_date):

    date = parse_datetime(s_date)

    posts = BlogPost.objects.filter(publishstatus = 'public').filter(datepublished__lt = date).order_by('-datepublished')[:10]
    dict = {}
    dict['posts'] = posts


    last_date = BlogPost.objects.filter(publishstatus = 'public').order_by('-datepublished').values_list('datepublished', flat = True)[0]
    first_date = BlogPost.objects.filter(publishstatus = 'public').order_by('datepublished').values_list('datepublished', flat = True)[0]
    dict['first_date'] = first_date
    dict['last_date'] = last_date

    return render(request, 'magazine/all_posts.html', dict)

def f_allPosts_prev(request, s_date):
    date = parse_datetime(s_date)

    num_of_prev_posts = len(BlogPost.objects.filter(publishstatus = 'public').filter(datepublished__gt = date))
    num_of_posts_to_show = min(num_of_prev_posts, 10)
    start_from = num_of_prev_posts - num_of_posts_to_show
    posts = BlogPost.objects.filter(publishstatus = 'public').filter(datepublished__gt = date).order_by('-datepublished')[start_from:num_of_prev_posts]


    dict = {}
    dict['posts'] = posts


    last_date = BlogPost.objects.filter(publishstatus = 'public').order_by('-datepublished').values_list('datepublished', flat = True)[0]
    first_date = BlogPost.objects.filter(publishstatus = 'public').order_by('datepublished').values_list('datepublished', flat = True)[0]
    dict['first_date'] = first_date
    dict['last_date'] = last_date

    return render(request, 'magazine/all_posts.html', dict)

def f_allPosts_by_author_next(request, s_date, author_username):
    date = parse_datetime(s_date)

    posts = BlogPost.objects.filter(publishstatus = 'public').filter(author__username = author_username).filter(datepublished__lt = date).order_by('-datepublished')[:10]
    dict = {}
    dict['posts'] = posts


    last_date = BlogPost.objects.filter(publishstatus = 'public').filter(author__username = author_username).order_by('-datepublished').values_list('datepublished', flat = True)[0]
    first_date = BlogPost.objects.filter(publishstatus = 'public').filter(author__username = author_username).order_by('datepublished').values_list('datepublished', flat = True)[0]
    dict['first_date'] = first_date
    dict['last_date'] = last_date
    dict['author_username'] = author_username
    return render(request, 'magazine/all_posts_by_author.html', dict)

def f_allPosts_by_author_prev(request, s_date, author_username):

    date = parse_datetime(s_date)

    num_of_prev_posts = len(BlogPost.objects.filter(publishstatus = 'public').filter(author__username = author_username).filter(datepublished__gt = date))
    num_of_posts_to_show = min(num_of_prev_posts, 10)
    start_from = num_of_prev_posts - num_of_posts_to_show
    posts = BlogPost.objects.filter(publishstatus = 'public').filter(author__username = author_username).filter(datepublished__gt = date).order_by('-datepublished')[start_from:num_of_prev_posts]


    dict = {}
    dict['posts'] = posts


    last_date = BlogPost.objects.filter(publishstatus = 'public').filter(author__username = author_username).order_by('-datepublished').values_list('datepublished', flat = True)[0]
    first_date = BlogPost.objects.filter(publishstatus = 'public').filter(author__username = author_username).order_by('datepublished').values_list('datepublished', flat = True)[0]
    dict['first_date'] = first_date
    dict['last_date'] = last_date
    dict['author_username'] = author_username

    return render(request, 'magazine/all_posts_by_author.html', dict)


class MagazineHome(ListView):
    model = BlogPost
    template_name = 'magazine/magazine.html'


    def get_context_data(self, **kwargs):
        context = super(MagazineHome, self).get_context_data(**kwargs)


        last_date = BlogPost.objects.filter(publishstatus = 'public').order_by('-datepublished').values_list('datepublished', flat= True)[0]
        days_to_add = 1
        last_date = last_date + timedelta(days=days_to_add)
        context['last_date'] = last_date

        context['main_post']   = BlogPost.objects.filter(publishstatus = 'public').order_by('-datepublished')[0]
        context['most_relveant'] = BlogPost.objects.filter(publishstatus = 'public').order_by('-datepublished')[1:4]
        context['object_list'] = BlogPost.objects.filter(publishstatus = 'public').order_by('-datepublished')[4:8]
        num_of_main_posts = 8
        min_num_of_posts = 7
        authors =  BlogPost.objects.filter(publishstatus = 'public').order_by('-datepublished').filter(Q(author__groups__name = 'admin') | Q(author__groups__name = 'owner')).values_list('author__id').annotate(total=Count('author__id')).distinct().order_by()
        authors_id = []

        for author in authors:
            auhtor_count = author[1]
            if (auhtor_count >= min_num_of_posts):
                authors_id.append(author[0])
            #if (auhtor_count > min_num_of_posts + num_of_main_posts):
            #    authors_id.append(author[0])

        first_8_posts = BlogPost.objects.filter(publishstatus = 'public').order_by('-datepublished')[0:8]
        context['authors_posts'] = []

        used_posts = []
        used_posts.append(first_8_posts)
        for author_id in authors_id:
            #posts of author not in the first 15 posts
            #(not that the number 15 can cahnge with website update)
            #(this is why i use variables such num_of_main_posts  and min_num_of_posts)
            #(instead of hardcore number)
            posts_of_author= BlogPost.objects.filter(publishstatus = 'public').order_by('-datepublished').filter(author__id = author_id).exclude(id__in=first_8_posts)[0:min_num_of_posts]
            if(posts_of_author.count() >= 7):
                context['authors_posts'].append(posts_of_author)
                used_posts.append(posts_of_author)

            #context['authors_posts'].append(BlogPost.objects.filter(publishstatus = 'public').order_by('-datepublished').filter(author__id = author_id)[num_of_main_posts + 1:][:min_num_of_posts])


        not_used_posts = BlogPost.objects.filter(publishstatus = 'public').order_by('-datepublished')
        for posts_by_author in used_posts:
            not_used_posts  = not_used_posts.exclude(id__in = posts_by_author)

        min_num_posts_per_label = 4
        posts_by_labels = []
        labels =  Labels.objects.all().values_list('id', 'text').distinct().order_by()
        stored_labels_to_html = []
        for label in labels:
            posts_of_label = not_used_posts.filter(id__in = Labels.objects.filter(id=label[0]).values_list('articles'))
            if(posts_of_label.count() >= min_num_posts_per_label):
                posts_by_labels.append(posts_of_label[0:min_num_posts_per_label])
                stored_labels_to_html.append(label)

        zipped_lst = []
        zipped_lst = zip(posts_by_labels, stored_labels_to_html)
        context['posts_by_labels'] = zipped_lst

        #signal
        try:
            user = self.request.user
            user_visit_site.send(user.__class__, instance = user, request = self.request)
        except:
            pass

        return context


def rate_post(request, pk):
    post = get_object_or_404(BlogPost, id = pk)
    if 'like-btn' in request.POST:
        is_already_liked = post.likes.filter(id = request.user.id).exists()
        if is_already_liked:
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)
            post.dislikes.remove(request.user)
            notification = Notification.objects.create(notification_type = 1, from_user = request.user, post = post, to_user = post.author)

    elif 'dislike-btn' in request.POST:
        is_already_disliked = post.dislikes.filter(id = request.user.id).exists()
        if is_already_disliked:
            post.dislikes.remove(request.user)
        else:
            post.dislikes.add(request.user)
            post.likes.remove(request.user)
            notification = Notification.objects.create(notification_type = 4, from_user = request.user, post = post, to_user = post.author)
    return HttpResponseRedirect(reverse('magazine:anArticle', args = [str(pk)]))

def rate_com(request, pk):
    com = get_object_or_404(Comment, id = pk)
    if 'like-com' in request.POST:
        is_already_liked = com.likes.filter(id = request.user.id).exists()
        if is_already_liked:
            com.likes.remove(request.user)
        else:
            com.likes.add(request.user)
            com.dislikes.remove(request.user)
            notification = Notification.objects.create(notification_type = 1, from_user = request.user, comment = com, to_user = com.comment_usr)

    elif 'dislike-com' in request.POST:
        is_already_disliked = com.dislikes.filter(id = request.user.id).exists()
        if is_already_disliked:
            com.dislikes.remove(request.user)
        else:
            com.dislikes.add(request.user)
            com.likes.remove(request.user)
            notification = Notification.objects.create(notification_type = 4, from_user = request.user, comment = com, to_user = com.comment_usr)
    return HttpResponseRedirect(reverse('magazine:anArticle', args = [str(com.post.id), '-replace-me-comment'+ str(com.id)]))

def rate_com_of_com(request, pk):
    com_of_com = get_object_or_404(comment_of_comment, id = pk)
    if 'like-com-of-com' in request.POST:
        is_already_liked = com_of_com.likes.filter(id = request.user.id).exists()
        if is_already_liked:
            com_of_com.likes.remove(request.user)
        else:
            com_of_com.likes.add(request.user)
            com_of_com.dislikes.remove(request.user)
            notification = Notification.objects.create(notification_type = 1, from_user = request.user, com_of_com = com_of_com, to_user = com_of_com.comment_of_comment_usr)

    elif 'dislike-com-of-com' in request.POST:
        is_already_disliked = com_of_com.dislikes.filter(id = request.user.id).exists()
        if is_already_disliked:
            com_of_com.dislikes.remove(request.user)
        else:
            com_of_com.dislikes.add(request.user)
            com_of_com.likes.remove(request.user)
            notification = Notification.objects.create(notification_type = 4, from_user = request.user, com_of_com = com_of_com, to_user = com_of_com.comment_of_comment_usr)
    return HttpResponseRedirect(reverse('magazine:anArticle', args = [str(com_of_com.comment.post.id), '-replace-me-sub-comment'+ str(com_of_com.id)]))


@check_if_post_accessible
def Article(request, pk, pos_id = '#start'):


    comment_frm = CommentFrm(request.POST or None, request.FILES or None, prefix="com")
    com_of_com_frm = comment_of_comment_frm(request.POST or None, request.FILES or None, prefix="subcom")

    post = BlogPost.objects.get(pk = pk)

    total_likes = post.total_likes()
    total_dislikes = post.total_dislikes()
    liked = False
    disliked = False
    if request.user.is_authenticated:
        liked = post.likes.filter(id = request.user.id).exists()
        disliked = post.dislikes.filter(id = request.user.id).exists()

    if request.method == 'POST' and request.user.is_authenticated:
        if 'btn-send-comment' in request.POST:
            if comment_frm.is_valid():
                comment_frm.instance.post = post #request.post
                if(request.user.id):
                    comment_frm.instance.comment_usr = request.user
                com_obj = comment_frm.save()
                if request.user.is_authenticated:
                    notification = Notification.objects.create(notification_type = 2, from_user = request.user, comment = com_obj, to_user = post.author)
                else:
                    notification = Notification.objects.create(notification_type = 2, comment = com_obj, to_user = post.author)
                follow_post_by_sending_com(com = com_obj)
                tag_user(com_obj)
                replaceTaggedUsersToTaggedElemesInCom(com_obj)
                dict = {'pos_id':pos_id, 'object':post, 'comment_frm':comment_frm, 'com_of_com_frm':com_of_com_frm , 'status':'posted', 'com_obj':com_obj, 'total_likes':total_likes, 'total_dislikes':total_dislikes, 'liked':liked, 'disliked' :disliked}
                return render(request, 'magazine/article.html', dict )

        if 'btn-reply-comment-of-comment' in request.POST:
            if com_of_com_frm.is_valid():
                comment_id = request.POST.get('comment_id')
                comment = Comment.objects.get(pk = comment_id)
                com_of_com_frm.instance.comment = comment
                if(request.user.id):
                    com_of_com_frm.instance.comment_of_comment_usr = request.user
                com_of_com  = com_of_com_frm.save()
                if request.user.is_authenticated:
                    notification = Notification.objects.create(notification_type = 2, from_user = request.user, com_of_com = com_of_com, to_user = comment.comment_usr)
                else:
                    notification = Notification.objects.create(notification_type = 2, com_of_com = com_of_com, to_user = comment.comment_usr)
                dict = {'pos_id':pos_id, 'object':post, 'comment_frm':comment_frm, 'com_of_com_frm':com_of_com_frm , 'status':'posted', 'com_obj':comment, 'total_likes':total_likes, 'total_dislikes':total_dislikes, 'liked':liked, 'disliked' :disliked}
                return render(request, 'magazine/article.html', dict)

    dict = {'pos_id':pos_id, 'object':post,  'comment_frm':comment_frm, 'com_of_com_frm':com_of_com_frm , 'status':'not-posted', 'total_likes':total_likes, 'total_dislikes':total_dislikes, 'liked':liked, 'disliked' :disliked}
    return render(request, 'magazine/article.html', dict)



@unauthenticated_user
@allowed_users(allowed_roles = ['owner', 'admin'])
def fUpdateRecord(request, id):
    obj = get_object_or_404(BlogPost, id = id)
    prev_publish_status = obj.publishstatus
    frm = BlogPostForm(request.POST or None, request.FILES or None, instance = obj)
    if(request.method == 'POST'):
        if frm.is_valid():
            if 'btnSave' in request.POST:
                post_obj = frm.save()
                to_notify_users_for_new_post(request.user, post_obj, prev_publish_status)
            elif 'btndelete' in request.POST:
                obj.delete()
            return redirect('magazine:magazineNews')
    return render(request, 'magazine/editPosts.html', {'frm':frm, 'post':obj})





def fgetpostsbyauthor(request):
    posts = BlogPost.objects.all().filter(author_id = request.user.id).order_by('-datepublished')
    #BlogFormset = modelformset_factory(BlogPost, fields = ['title', 'subtitle', 'content', 'publishstatus', 'thumb'])
    #form_set = BlogFormset(queryset= BlogPost.objects.all())

    """
    Changing the queryset¶
    By default, when you create a formset from a model, the formset will use a queryset that includes
    all objects in the model (e.g., Author.objects.all()). You can override this behavior by using the queryset argument:
     >>> formset = AuthorFormSet(queryset=Author.objects.filter(name__startswith='O'))

    """

    #data = {'data' : zip(posts, form_set)}
    return render(request, 'magazine/displayPosts.html', {'posts':posts})


def fskeleton(request):
    return render(request, 'magazine/base.html', {})

@unauthenticated_user
@allowed_users(allowed_roles = ['owner', 'admin'])
def fwriteblog(request):
    if request.method == 'POST':
        frm = BlogPostForm(request.POST, request.FILES)
        if frm.is_valid():
            post_obj = frm.save()
            to_notify_users_for_new_post(request.user, post_obj)
            return redirect('magazine:magazineNews')

    frm = BlogPostForm()
    context = {
    'frm':frm
    }
    return render(request, 'magazine/writepost.html', context)

def to_notify_users_for_new_post(user, post, prev_publish_status=None):
    publishstatus = post.publishstatus
    if(publishstatus == 'private'):
        return
    if(prev_publish_status == 'public'):
        return
    notify_users_for_new_post(user, post)

def get_labels_for_post_ajax(request):
    if not request.user.is_authenticated:
        return JsonResponse({'status':'not-log-in'})
    if request.is_ajax and request.method == "GET":
        #username = request.GET.get('username')
        is_user_admin = False
        is_user_owner = False
        groups = list(request.user.groups.values_list('name',flat = True))
        if 'admin' in groups or 'owner' in groups:
            is_user_admin = True
        if 'owner' in groups:
            is_user_owner = True
        post_id = request.GET.get('post_id')
        post_user = get_post_author(post_id)
        if(post_user != request.user and is_user_owner == False):
            return JsonResponse({'status':'acesss is denied'})
        if(is_user_admin == False and is_user_owner == False):
            return JsonResponse({'status':'acesss is denied'})
        cblist_of_what = request.GET.get('cblist_of_what')
        lst_labels = get_post_labels(post_id, cblist_of_what)
        return JsonResponse(lst_labels, safe = False)



def update_cblist_for_post_ajax(request):
    if not request.user.is_authenticated:
        return JsonResponse({'status':'not-log-in'})
    if request.is_ajax and request.method == "POST":
        #username = request.GET.get('username')
        is_user_admin = False
        is_user_owner = False
        groups = list(request.user.groups.values_list('name',flat = True))
        if 'admin' in groups or 'owner' in groups:
            is_user_admin = True
        if 'owner' in groups:
            is_user_owner = True
        post_id = request.POST.get('post_id')
        post_user = get_post_author(post_id)
        if(post_user != request.user and is_user_owner == False):
            return JsonResponse({'status':'acesss is denied'})
        if(is_user_admin == False and is_user_owner == False):
            return JsonResponse({'status':'acesss is denied'})

        label_id = request.POST.get('label_id')
        is_checked = request.POST.get('is_checked')
        cblist_of_what = request.POST.get('cblist_of_what')
        update_post_labels(post_id, is_checked, label_id, cblist_of_what)
        return JsonResponse({'status':'succeeded'})

def create_new_label_ajax(request):
    if not request.user.is_authenticated:
        return JsonResponse({'status':'not-log-in'})
    if request.is_ajax and request.method == "POST":
        #username = request.GET.get('username')
        is_user_admin = False
        is_user_owner = False
        groups = list(request.user.groups.values_list('name',flat = True))
        if 'admin' in groups or 'owner' in groups:
            is_user_admin = True
        if 'owner' in groups:
            is_user_owner = True
        post_id = request.POST.get('post_id')
        post_user = get_post_author(post_id)
        if(post_user != request.user and is_user_owner == False):
            return JsonResponse({'status':'acesss is denied'})
        if(is_user_admin == False and is_user_owner == False):
            return JsonResponse({'status':'acesss is denied'})

        txt = request.POST.get('txt')
        cblist_of_what = request.POST.get('cblist_of_what')
        result = create_new_label_for_post(post_id, txt, cblist_of_what)
        return JsonResponse(result)


def update_label_name_ajax(request):
    if not request.user.is_authenticated:
        return JsonResponse({'status':'not-log-in'})
    if request.is_ajax and request.method == "POST":
        #username = request.GET.get('username')
        is_user_owner = False
        groups = list(request.user.groups.values_list('name',flat = True))
        if 'owner' in groups:
            is_user_owner = True
        if(is_user_owner == False):
            return JsonResponse({'status':'acesss is denied'})

        txt = request.POST.get('txt')
        id = request.POST.get('label_id')
        update_label_name(id, txt)
        return JsonResponse({'status':'succeeded'})

def remove_label_ajax(request):
    if not request.user.is_authenticated:
        return JsonResponse({'status':'not-log-in'})
    if request.is_ajax and request.method == "POST":
        #username = request.GET.get('username')
        is_user_owner = False
        groups = list(request.user.groups.values_list('name',flat = True))
        if 'owner' in groups:
            is_user_owner = True
        if(is_user_owner == False):
            return JsonResponse({'status':'acesss is denied'})

        id = request.POST.get('label_id')
        remove_label(id)
        return JsonResponse({'status':'succeeded'})


#update_label_name, remove_label
