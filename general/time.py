from django.utils import timezone
from datetime import timedelta
from dateutil import relativedelta

def FriendlyTimePassedView(d):
    years = get_years_passed(d)
    if(years >= 1):
        return {'unit':'years', 'cnt':years}
    months = get_months_passed(d)
    if(months >= 1):
        return {'unit':'months', 'cnt':months}

    weeks = get_weeks_passed(d)
    if(weeks >= 1):
        return {'unit':'weeks', 'cnt':weeks}

    days  = get_days_passed(d)
    if(days >=1):
        return {'unit':'days', 'cnt':days}

    hours = get_hours_passed(d)
    if(hours >= 1):
        return {'unit':'hours', 'cnt':hours}

    miniutes = get_miniutes_passed(d)
    return {'unit':'miniutes', 'cnt':miniutes}





def get_now_time():
    return timezone.now()

def get_miniutes_passed(d_start):
    d_end = get_now_time()
    minutes_passed = get_delta_dates_in_minutes(d_end, d_start)
    return minutes_passed

def get_weeks_passed(d):
    days = get_days_passed(d)
    return int(days/7)

def get_hours_passed(d_start):
    d_end = get_now_time()
    hours_passed = get_delta_dates_in_hours(d_end, d_start)
    return hours_passed

def get_days_passed(d_start):
    d_end = get_now_time()
    days_passed = get_delta_dates_in_days(d_end, d_start)
    return days_passed

def get_months_passed(d_start):
    d_end = get_now_time()
    months_passed = get_delta_dates_in_months(d_end, d_start)
    return months_passed


def get_delta_dates_in_days(d_end, d_start):
    delta = d_end - d_start
    return delta.days

def get_delta_dates_in_hours(d_end, d_start):
    return int(get_delta_dates_in_minutes(d_end, d_start)/60)

def get_delta_dates_in_minutes(d_end, d_start):
    return int(get_delta_dates_in_seconds(d_end, d_start)/60)

def get_delta_dates_in_seconds(d_end, d_start):
    delta = d_end - d_start
    return delta.total_seconds()


def get_years_passed(d_start):
    d_end = get_now_time()
    return get_delta_dates_in_years(d_end, d_start)

def get_delta_dates_in_years(d_end, d_start):

    delta = relativedelta.relativedelta(d_end, d_start)
    years = delta.years
    #res_months = delta.months + (delta.years * 12)
    return years

def get_delta_dates_in_months(d_end, d_start):

    delta = relativedelta.relativedelta(d_end, d_start)
    years = delta.years
    res_months = delta.months + (delta.years * 12)
    return res_months
