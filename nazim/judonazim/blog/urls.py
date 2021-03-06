
"""judonazim URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from blog import urls
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

app_name = 'blog'
urlpatterns = [

 path('', views.fhome, name = 'homepage' ),
 path('blank', views.fblank, name = 'blank' ),
 path('base/', views.fbase, name = 'basehtml' ),
 #path('blog/<str:slug>/', views.fwriteblog, name = 'blogfrm' ),
 path('blog/', views.fwriteblog, name = 'blogfrm' ),
 path('texteditorbase/', views.ftxteditor, name = 'edtxt' ),
 #path('admin/', admin.site.urls)
]
