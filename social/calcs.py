from datetime import datetime


def get_total_seconds(date1, date2):
    date_1 = str(date1)
    date_2 = str(date2)
    date_format_str = '%Y-%m-%d %H:%M:%S.%f'
    end = datetime.strptime(date_1, date_format_str)
    start =   datetime.strptime(date_2, date_format_str)
    # Get the interval between two datetimes as timedelta object
    diff = end - start
    print('Difference between two datetimes in seconds:')
    print(diff.total_seconds())
    return diff.total_seconds()

def get_curr_datetime():
    return datetime.now()
