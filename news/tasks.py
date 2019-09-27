from celery import task
from celery.decorators import periodic_task

@periodic_task(run_every=5)
def del_redis_data():
    print("清除redis缓存")