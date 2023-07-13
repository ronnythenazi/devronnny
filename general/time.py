from django.utils import timezone
from datetime import timedelta


def get_now_time():
    return timezone.now()

def get_miniutes_passed(d_start):
    d_end = get_now_time()
    minutes_passed = get_delta_dates_in_minutes(d_end, d_start)
    return minutes_passed

def get_hours_passed(d_start):
    d_end = get_now_time()
    hours_passed = get_delta_dates_in_hours(d_end, d_start)
    return hours_passed

def get_days_passed(d_start):
    d_end = get_now_time()
    days_passed = get_delta_dates_in_days(d_end, d_start)
    return days_passed

def get_delta_dates_in_days(d_end, d_start):
    delta = d_end - d_start
    return delta.total_days()

def get_delta_dates_in_hours(d_end, d_start):
    return int(get_delta_dates_in_minutes(d_end, d_start)/60)

def get_delta_dates_in_minutes(d_end, d_start):
    return int(get_delta_dates_in_seconds(d_end, d_start)/60)

def get_delta_dates_in_seconds(d_end, d_start):
    delta = d_end - d_start
    return delta.total_seconds()
