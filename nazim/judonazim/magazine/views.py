from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.views.generic import ListView, DetailView #, CreateView
from .models import BlogPost
from django.urls import reverse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .blogpublishing import *
from django.forms import modelformset_factory

#post = get_object_or_404(BlogPost)

class MagazineHome(ListView):
    model = BlogPost
    template_name = 'magazine/magazine.html'

class Article(DetailView):
    model = BlogPost
    template_name = 'magazine/article.html'

def fgetpostsbyauthor(request):
    posts = BlogPost.objects.all()

    """
     Changing the queryset¶

    By default, when you create a formset from a model, the formset will use a queryset that includes
    all objects in the model (e.g., Author.objects.all()). You can override this behavior by using the queryset argument:

   >>> formset = AuthorFormSet(queryset=Author.objects.filter(name__startswith='O'))


    """
    BlogFormset = modelformset_factory(BlogPost, fields = ['title', 'subtitle', 'content', 'publishstatus'])
    form_set = BlogFormset(queryset= BlogPost.objects.all())

    """
    frms = frm_set(instance = posts)
    frms = []
    for post in posts:
        frm = BlogPostForm(request.POST or None, instance = post)
        frms.append(frm)


    data = {'data' : zip(posts, frms)}
    """
    data = {'data' : zip(posts, form_set)}
    return render(request, 'magazine/editPosts.html', data)


def fskeleton(request):
    return render(request, 'magazine/base.html', {})

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
