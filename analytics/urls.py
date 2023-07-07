from django.urls import path, include
#from magazine import urls
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import  *

app_name = 'analytics'

urlpatterns = [
path('set_visitor_date_for_post_ajax', set_visitor_date_for_post_ajax ,name='set_visitor_date_for_post_ajax'),
path('set_visitor_date_for_homepage_ajax', set_visitor_date_for_homepage_ajax ,name='set_visitor_date_for_homepage_ajax'),
path('get_anonymous_visitors_for_post_ajax', get_anonymous_visitors_for_post_ajax ,name='get_anonymous_visitors_for_post_ajax'),
path('get_member_visitors_for_post_ajax', get_member_visitors_for_post_ajax ,name='get_member_visitors_for_post_ajax'),
path('get_anonymous_visitors_ajax', get_anonymous_visitors_ajax ,name='get_anonymous_visitors_ajax'),
path('get_member_visitors_ajax', get_member_visitors_ajax ,name='get_member_visitors_ajax'),

]
