from django.urls import path, include
#from magazine import urls
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views
from .views import MagazineHome, Article, Comment, f_allPosts_next, f_allPosts_prev, f_allPosts_by_author_next, f_allPosts_by_author_prev
from users.views import login_view
#from django.contrib import admin
app_name = 'magazine'
urlpatterns = [
 path('', views.MagazineHome.as_view(), name = 'magazineNews' ),
 path('article/<int:pk>/',  views.Article, name = 'anArticle'),
 path('article/<int:pk>/<str:pos_id>', views.Article, name = 'anArticle'),
 path('base/', views.fskeleton, name = 'MagazineCtlSkeleton'),
 #path('ShareYouThoughs/', views.AddPost.as_view(), name = 'enlightThePublic'),
 path('ShareYouThoughs/', views.fwriteblog, name = 'enlightThePublic'),
 path('myposts/', views.fgetpostsbyauthor, name = 'myposts'),
 path('update/<int:id>', views.fUpdateRecord, name = 'updateRecord'),
 path('manageUserAndGroups/', views.manageUsersPermission, name = 'userRoles'),
 path('allposts-next/<str:s_date>/', views.f_allPosts_next, name = 'more_posts_next'),
 path('allposts-prev/<str:s_date>/', views.f_allPosts_prev, name = 'more_posts_prev'),

 path('allposts-by-author-next/<str:s_date>/<str:author_username>', views.f_allPosts_by_author_next, name = 'more_posts_by_author_next'),
 path('allposts-by-author-prev/<str:s_date>/<str:author_username>', views.f_allPosts_by_author_prev, name = 'more_posts_by_author_prev'),

 path('rate-post/<int:pk>', views.rate_post, name = 'rate_post'),
 path('rate-com/<int:pk>', views.rate_com, name = 'rate_com'),
 path('rate-com-of-com/<int:pk>', views.rate_com_of_com, name = 'rate_com_of_com'),
 path('about-ronny-the-nazi/', views.about_ronny_the_nazi , name="about_ronny_the_nazi"),
 path('login/', login_view, name = 'login'),
 path('deactivate_user/', views.deactivate_user_ajax, name='deactivate_user'),
 path('activate_user/', views.activate_user_ajax, name='activate_user'),
 path('search-results-articles/', views.search_articles, name='search-articles'),
 path('load-more-matched-articles/', views.load_more_matched_articles_ajax, name='load-more-matched-articles'),
 path('get-cblist-article-ajax', views.get_labels_for_post_ajax , name = 'get-cblist-ajax'),
 path('update-cblist-ajax', views.update_cblist_for_post_ajax , name = 'update-cblist-ajax'),
 path('create-new-label-ajax', views.create_new_label_ajax , name = 'create-new-label-ajax'),
 path('remove-label-ajax', views.remove_label_ajax, name = 'remove-label-ajax'),
 path('update-label-name-ajax', views.update_label_name_ajax, name = 'update-label-name-ajax'),
 path('quick-delete-label-item-ajax', views.remove_label_ajax, name ='quick-delete-label-item-ajax'),
]
