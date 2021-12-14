from django.shortcuts import render
from django.views.generic import ListView, DetailView #, CreateView
from .models import BlogPost
from django.urls import reverse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .blogpublishing import *


class MagazineHome(ListView):
    model = BlogPost
    template_name = 'magazine/magazine.html'

class Article(DetailView):
    model = BlogPost
    template_name = 'magazine/article.html'
"""
class AddPost(CreateView):
    model = BlogPost
    template_name = 'magazine/writepost.html'
    fields = '__all__'
"""
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
