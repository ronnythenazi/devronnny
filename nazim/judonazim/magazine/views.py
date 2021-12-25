from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, Http404
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
    #ordering = ['-datepublished']

    def get_context_data(self, **kwargs):
        context = super(MagazineHome, self).get_context_data(**kwargs)
        context['object_list'] = BlogPost.objects.all().filter(publishstatus = 'public').order_by('-datepublished')
        return context

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
