from django.shortcuts import render, redirect

# Create your views here.
def global_home(request):
    return redirect('blog:fblank')
