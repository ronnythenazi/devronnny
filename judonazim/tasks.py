import os
import urllib.parse
from redis import Redis
#from rq import Worker, Queue, Connection
from django.conf import settings
from workers import task

'''
@task()
def connect_to_redis_server():
    print('this is the first task ever horrey')
    listen = ['high', 'default', 'low']

    redis_url = settings.REDIS_URL
    if not redis_url:
        raise RuntimeError('Set up Redis To Go first.')

    urllib.parse.uses_netloc.append('redis')
    url = urllib.parse(redis_url)
    conn = Redis(host=url.hostname, port=url.port, db=0, password=url.password)

    if __name__ == '__main__':
        with Connection(conn):
            worker = Worker(map(Queue, listen))
            worker.work()
'''

'''
@task(schedule=10)
def do_something():
    print('I run every 10 seconds')

@task(schedule=60*5)
def do_something_later():
    print('I run every 5 minutes')

@task(schedule=60*60*8)
def do_something_even_later():
    print('I run every 8 hours')
'''
