from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, Http404, redirect
from django.views.generic import ListView, DetailView , CreateView
from .models import BlogPost, Profile
from django.urls import reverse
from django.http import HttpResponse
from .blogpublishing import *
from django.forms import modelformset_factory
from .decorations import unauthenticated_user, allowed_users, check_if_post_accessible


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


class MagazineHome(ListView):
    model = BlogPost
    template_name = 'magazine/magazine.html'
    #ordering = ['-datepublished']

    def get_context_data(self, **kwargs):
        context = super(MagazineHome, self).get_context_data(**kwargs)
        context['object_list'] = BlogPost.objects.all().filter(publishstatus = 'public').order_by('-datepublished')
        return context
"""
class Article(DetailView):
    model = BlogPost
    template_name = 'magazine/article.html'
    def get_queryset(self):
        qs = super(Article, self).get_queryset()
        return qs.filter(publishstatus = 'public')

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            # redirect here
            return redirect('magazine:magazineNews')
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)

"""
@check_if_post_accessible
def Article(request, pk):
    comment_frm = CommentFrm(request.POST or None)
    post = BlogPost.objects.get(pk = pk)
    if request.method == 'POST':
        if 'btn-send-comment' in request.POST:
            if comment_frm.is_valid():
                comment_frm.instance.post = post#request.post
                if(request.user.id):
                    comment_frm.instance.comment_usr = request.user
                com_obj = comment_frm.save()
                return render(request, 'magazine/article.html', {'object':post, 'comment_frm':comment_frm, 'status':'posted', 'com_obj':com_obj})
    return render(request, 'magazine/article.html', {'object':post, 'comment_frm':comment_frm, 'status':'not-posted'})

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
