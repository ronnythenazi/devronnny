from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import global_home


app_name = 'general'
urlpatterns = [
  path('', global_home, name = 'my_global_home'),

]
