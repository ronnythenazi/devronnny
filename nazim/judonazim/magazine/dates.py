from .models import BlogPost
from django.utils.dateparse import parse_datetime
import datetime

def get_first_date_str():
    return date_to_format_str(BlogPost.objects.values_list('datepublished', flat = True).order_by('datepublished')[0])

def date_to_format_str(date):
    s_date = str(date)
    date_f = datetime.datetime.strptime(s_date, "%Y-%m-%d %H:%M:%S")
    return str(date_f)
