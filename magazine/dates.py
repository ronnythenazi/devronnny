from .models import BlogPost
from django.utils.dateparse import parse_datetime
import datetime
from dateutil import relativedelta



def omit_time_from_datetime(date_with_time):
    return date_with_time.date()

def get_first_date_str():
    return date_to_format_str(BlogPost.objects.values_list('datepublished', flat = True).order_by('datepublished')[0])

def date_to_format_str(date):
    s_date = str(date)
    date_f = datetime.datetime.strptime(s_date, "%Y-%m-%d %H:%M:%S")
    return str(date_f)

def get_curr_datetime():
    return datetime.datetime.now()

def get_curr_s_datetime():
    return str(get_curr_datetime())


def get_total_date_diff_hours(date_start, date_end):
    total_hours = get_total_diff_seconds(date_start, date_end) / 3600

    return total_hours

def get_total_diff_minutes(date_start, date_end):
    total_minutes = get_total_diff_seconds(date_start, date_end) / 60

    return total_minutes

def get_total_diff_days(date_start, date_end):
    s_date_start = str(date_start)
    s_date_end = str(date_end)
    date_format_str = '%d/%m/%Y'
    f_date_end = datetime.datetime.strptime(s_date_end, date_format_str)
    f_date_start =   datetime.datetime.strptime(s_date_start, date_format_str)
    diff = f_date_end.date() - f_date_start.date()
    total_days = diff.days


    return total_days

def get_total_diff_weeks(date_start, date_end):
    days_gap =  get_total_diff_days(date_start, date_end)
    total_weeks = days_gap / 168

    return total_weeks

def get_date_diff_months(date_start, date_end):
    s_date_start = str(date_start)
    s_date_end = str(date_end)
    date_format_str = '%d/%m/%Y'
    f_date_end = datetime.datetime.strptime(s_date_end, date_format_str)
    f_date_start =   datetime.datetime.strptime(s_date_start, date_format_str)
    diff = relativedelta.relativedelta(f_date_end, f_date_start)

    return diff.months

def get_date_diff_years(date_start, date_end):
    s_date_start = str(date_start)
    s_date_end = str(date_end)
    date_format_str = '%d/%m/%Y'
    f_date_end = datetime.datetime.strptime(s_date_end, date_format_str)
    f_date_start =   datetime.datetime.strptime(s_date_start, date_format_str)
    diff = relativedelta.relativedelta(f_date_end, f_date_start)

    return diff.years

def get_total_diff_seconds(date_start, date_end):
    s_date_start = str(date_start)
    s_date_end = str(date_end)
    date_format_str = '%Y-%m-%d %H:%M:%S.%f'
    f_date_end = datetime.datetime.strptime(s_date_end, date_format_str)
    f_date_start =   datetime.datetime.strptime(s_date_start, date_format_str)
    diff = f_date_end - f_date_start
    total_seconds = diff.total_seconds()

    return total_seconds
