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

from django.urls import path, include, re_path
from blog import urls
from magazine import urls
from social import urls
from general import urls
from analytics import urls
from notifications import urls
from chats import urls
from staticpages import urls
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from ckeditor_uploader import views as uploader_views
from django.views.decorators.cache import never_cache


if settings.DEBUG:
    from django.contrib import admin



if settings.DEBUG:
    urlpatterns = [
        path('info/', include('blog.urls')),
        path('admin/', admin.site.urls),
        #path('magazine/', include('magazine.urls')),
        path('', include('magazine.urls')),
        path('social/', include('social.urls')),
        path('general/', include('general.urls')),
        path('users/', include('django.contrib.auth.urls')),
        path('users/', include('users.urls')),
        path('analytics/', include('analytics.urls')),
        path('chats/', include('chats.urls')),
        path('staticpages/', include('staticpages.urls')),
        path('notifications/', include('notifications.urls')),
        #url(r'^ckeditor/', include('ckeditor_uploader.urls')),
        url(r'^ckeditor/upload/',uploader_views.upload, name='ckeditor_upload'),
        url(r'^ckeditor/browse/',never_cache(uploader_views.browse), name='ckeditor_browse'),

        # added in 21-08-2023 21:33
        url(r'^ckeditor/', include('ckeditor_uploader.urls')),
        path('accounts/', include('allauth.urls')),
        path('admin/defender/', include('defender.urls')),
        url(r'^webpush/', include('webpush.urls')),





    ] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
    '''urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT
        }),
    ]'''



else:
    urlpatterns = [
      path('info/', include('blog.urls')),
      #path('magazine/', include('magazine.urls')),
      path('', include('magazine.urls')),
      path('social/', include('social.urls')),
      path('general/', include('general.urls')),
      path('users/', include('django.contrib.auth.urls')),
      path('users/', include('users.urls')),
      path('analytics/', include('analytics.urls')),
      path('chats/', include('chats.urls')),
      path('staticpages/', include('staticpages.urls')),
      path('notifications/', include('notifications.urls')),
      #url(r'^ckeditor/', include('ckeditor_uploader.urls')),
      url(r'^ckeditor/upload/',uploader_views.upload, name='ckeditor_upload'),
      url(r'^ckeditor/browse/',never_cache(uploader_views.browse), name='ckeditor_browse'),

      # added in 21-08-2023 21:33
      url(r'^ckeditor/', include('ckeditor_uploader.urls')),
      path('accounts/', include('allauth.urls')),
      path('admin/defender/', include('defender.urls')),
      url(r'^webpush/', include('webpush.urls')),


    ]
