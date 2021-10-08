
from .blogpublishing import BlogPostForm
from .models import BlogPost
from django.urls import reverse
from django.shortcuts import render, redirect
from django.http import HttpResponse

def fwriteblog(request):
    frm = BlogPostForm(request.POST or None)
    if frm.is_valid():
        frm.save()
    context = {
    'frm':frm
    }
    return render(request, 'blogpost.html', context)


def fhome(request):
    if(request.method == 'POST'):
        if('btnnazimbg' in request.POST):
            obj = {'txtfilename':'nazimbg.html'}
            return render(request, 'index.html', {'txtfilename':'nazimbg.html'})
    return render(request, 'index.html', {'txtfilename':'nazimtaboo.html'})




def fbase(request):

    return render(request, 'base.html')

    #this line of codes create dirs and files in staticfile
    #in addition, it also example of sending data
    #from python code to html files#
    #result = storedata.fpublish_opinion()
    #mylist = {"output":result}
    #return render(request, 'debug.html',mylist)

    #return render(request, 'home.html')
    #return render(request, 'index.html')
    #return render(request, 'texteditor.html')
    #return render(request, 'static/plugins/mdb/src/index.html')
def ftxteditor(request):
    return render(request, 'texteditorbase.html')
    #return render(request, 'menuicon.html')
