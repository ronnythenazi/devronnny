from django.urls import path, include
#from magazine import urls
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views
from .views import MagazineHome, Article #, AddPost
#from django.contrib import admin
app_name = 'magazine'
urlpatterns = [
 path('', views.MagazineHome.as_view(), name = 'magazineNews' ),
 path('article/<int:pk>/', views.Article, name = 'anArticle'),
 path('base/', views.fskeleton, name = 'MagazineCtlSkeleton'),
 #path('ShareYouThoughs/', views.AddPost.as_view(), name = 'enlightThePublic'),
 path('ShareYouThoughs/', views.fwriteblog, name = 'enlightThePublic'),
 path('myposts/', views.fgetpostsbyauthor, name = 'myposts'),
 path('update/<int:id>', views.fUpdateRecord, name = 'updateRecord'),
]
