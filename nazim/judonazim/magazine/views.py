from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, Http404, redirect
from django.views.generic import ListView, DetailView , CreateView
from .models import BlogPost, Profile, Comment
from django.urls import reverse
from django.http import HttpResponse
from .blogpublishing import *
from django.forms import modelformset_factory
from .decorations import unauthenticated_user, allowed_users, check_if_post_accessible, check_if_post_and_comment_accessible
from django.db.models import Count, Q
from django.utils.dateparse import parse_datetime
from datetime import datetime, timedelta
from .dates import *
import math



#post = get_object_or_404(BlogPost)
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



def f_allPosts_next(request, s_date):

    date = parse_datetime(s_date)
    posts = BlogPost.objects.filter(datepublished__gt = date).order_by('datepublished')[:10]
    #date =  BlogPost.objects.filter(datepublished__gte = date).order_by('datepublished').values_list('datepublished', flat = True)[9]
    dict = {}
    dict['posts'] = posts
    #dict['s_date'] = date

    last_date = BlogPost.objects.all().order_by('-datepublished').values_list('datepublished', flat = True)[0]
    first_date = BlogPost.objects.all().order_by('datepublished').values_list('datepublished', flat = True)[0]
    dict['first_date'] = first_date
    dict['last_date'] = last_date

    return render(request, 'magazine/all_posts.html', dict)


def f_allPosts_prev(request, s_date):

    date = parse_datetime(s_date)
    num_of_prev_posts = len(BlogPost.objects.filter(datepublished__lt = date).order_by('-datepublished'))
    num_of_posts_to_show = min(num_of_prev_posts, 10)
    start_from = num_of_prev_posts - num_of_posts_to_show
    posts = BlogPost.objects.filter(datepublished__lt = date).order_by('datepublished')[start_from:num_of_prev_posts]
    #date =  BlogPost.objects.filter(datepublished__gte = date).order_by('datepublished').values_list('datepublished', flat = True)[9]
    dict = {}
    dict['posts'] = posts
    #dict['s_date'] = date

    last_date = BlogPost.objects.all().order_by('-datepublished').values_list('datepublished', flat = True)[0]
    first_date = BlogPost.objects.all().order_by('datepublished').values_list('datepublished', flat = True)[0]
    dict['first_date'] = first_date
    dict['last_date'] = last_date


    return render(request, 'magazine/all_posts.html', dict)




def f_allPosts_by_author_next(request, s_date, author_username):

    date = parse_datetime(s_date)
    posts = BlogPost.objects.filter(datepublished__gt = date).filter(author__username = author_username).order_by('datepublished')[:10]
    #date =  BlogPost.objects.filter(datepublished__gte = date).order_by('datepublished').values_list('datepublished', flat = True)[9]
    dict = {}
    dict['posts'] = posts
    #dict['s_date'] = date

    last_date = BlogPost.objects.filter(author__username = author_username).order_by('-datepublished').values_list('datepublished', flat = True)[0]
    first_date = BlogPost.objects.filter(author__username = author_username).order_by('datepublished').values_list('datepublished', flat = True)[0]
    dict['first_date'] = first_date
    dict['last_date'] = last_date
    dict['author_username'] = author_username

    return render(request, 'magazine/all_posts_by_author.html', dict)


def f_allPosts_by_author_prev(request, s_date, author_username):

    date = parse_datetime(s_date)
    num_of_prev_posts = len(BlogPost.objects.filter(datepublished__lt = date).filter(author__username = author_username).order_by('-datepublished'))
    num_of_posts_to_show = min(num_of_prev_posts, 10)
    start_from = num_of_prev_posts - num_of_posts_to_show
    posts = BlogPost.objects.filter(datepublished__lt = date).filter(author__username = author_username).order_by('datepublished')[start_from:num_of_prev_posts]
    #date =  BlogPost.objects.filter(datepublished__gte = date).order_by('datepublished').values_list('datepublished', flat = True)[9]
    dict = {}
    dict['posts'] = posts
    #dict['s_date'] = date

    last_date = BlogPost.objects.filter(author__username = author_username).order_by('-datepublished').values_list('datepublished', flat = True)[0]
    first_date = BlogPost.objects.filter(author__username = author_username).order_by('datepublished').values_list('datepublished', flat = True)[0]
    dict['first_date'] = first_date
    dict['last_date'] = last_date
    dict['author_username'] = author_username


    return render(request, 'magazine/all_posts_by_author.html', dict)

class MagazineHome(ListView):
    model = BlogPost
    template_name = 'magazine/magazine.html'


    def get_context_data(self, **kwargs):
        context = super(MagazineHome, self).get_context_data(**kwargs)

        first_date = BlogPost.objects.filter(publishstatus = 'public').order_by('datepublished').values_list('datepublished', flat= True)[0]
        days_to_subtract = 1
        first_date = first_date - timedelta(days=days_to_subtract)

        context['first_date'] = first_date

        context['main_post']   = BlogPost.objects.filter(publishstatus = 'public').order_by('-datepublished')[0]
        context['most_relveant'] = BlogPost.objects.filter(publishstatus = 'public').order_by('-datepublished')[1:4]
        context['object_list'] = BlogPost.objects.filter(publishstatus = 'public').order_by('-datepublished')[4:8]
        num_of_main_posts = 8
        min_num_of_posts = 6
        authors =  BlogPost.objects.filter(publishstatus = 'public').order_by('-datepublished').filter(Q(author__groups__name = 'admin') | Q(author__groups__name = 'owner')).values_list('author__id').annotate(total=Count('author__id')).distinct().order_by()
        authors_id = []
        #print(len(authors))
        #print(authors)
        for author in authors:
            auhtor_count = author[1]
            if (auhtor_count >= min_num_of_posts + num_of_main_posts):
                authors_id.append(author[0])
        #print(authors_id)

        context['authors_posts'] = []
        for author_id in authors_id:
            context['authors_posts'].append(BlogPost.objects.filter(publishstatus = 'public').order_by('-datepublished').filter(author__id = author_id)[9:][:min_num_of_posts])
        #content['author_pubs'] = BlogPost.objects.filter(publishstatus = 'public').order_by('-datepublished')[9:].order_by('author').annotate(authr_posts_num=Count('author', distinct=True)).filter(author__level__gte = 6)

        #print(context['authors_posts'][0][0]['pk'])
        return context


@check_if_post_accessible
def Article(request, pk):

    comment_frm = CommentFrm(request.POST or None)
    com_of_com_frm = comment_of_comment_frm(request.POST or None)

    post = BlogPost.objects.get(pk = pk)

    if request.method == 'POST':

        if 'btn-send-comment' in request.POST:

            if comment_frm.is_valid():

                comment_frm.instance.post = post #request.post
                if(request.user.id):
                    comment_frm.instance.comment_usr = request.user
                com_obj = comment_frm.save()
                return render(request, 'magazine/article.html', {'object':post, 'comment_frm':comment_frm, 'com_of_com_frm':com_of_com_frm , 'status':'posted', 'com_obj':com_obj})
        if 'btn-reply-comment-of-comment' in request.POST:
            if com_of_com_frm.is_valid():
                comment_id = request.POST.get('comment_id')
                comment = Comment.objects.get(pk = comment_id)
                com_of_com_frm.instance.comment = comment
                if(request.user.id):
                    com_of_com_frm.instance.comment_of_comment_usr = request.user
                com_of_com_frm.save()
                return render(request, 'magazine/article.html', {'object':post, 'comment_frm':comment_frm, 'com_of_com_frm':com_of_com_frm , 'status':'posted', 'com_obj':comment})



    return render(request, 'magazine/article.html', {'object':post,  'comment_frm':comment_frm, 'com_of_com_frm':com_of_com_frm , 'status':'not-posted'})



@unauthenticated_user
@allowed_users(allowed_roles = ['owner', 'admin'])
def fUpdateRecord(request, id):
    obj = get_object_or_404(BlogPost, id = id)
    frm = BlogPostForm(request.POST or None, request.FILES or None, instance = obj)
    if(request.method == 'POST'):
        if frm.is_valid():
            if 'btnSave' in request.POST:
                frm.save()
            elif 'btndelete' in request.POST:
                obj.delete()
            return redirect('magazine:magazineNews')
    return render(request, 'magazine/editPosts.html', {'frm':frm, 'post':obj})





def fgetpostsbyauthor(request):
    posts = BlogPost.objects.all().filter(author_id = request.user.id)
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
            frm.save()
            return redirect('magazine:magazineNews')

    frm = BlogPostForm()
    context = {
    'frm':frm
    }
    return render(request, 'magazine/writepost.html', context)
