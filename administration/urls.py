from django.urls import path, include
#from magazine import urls
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import (hideCommentAjax, unhideCommentAjax,)


app_name = 'administration'
urlpatterns = [
path('hideComment', hideCommentAjax, name = 'hideComment' ),
path('unhideComment', unhideCommentAjax, name = 'unhideComment' ),

]
