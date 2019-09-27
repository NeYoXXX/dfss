# from __future__ import absolute_import, unicode_literals
# import os
# from celery import Celery
#
# # 为celery程序设置环境为当前项目的环境
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dfss.settings')
# app = Celery('dfss')
#
# app.config_from_object('django.conf:settings', namespace='CELERY')
# app.autodiscover_tasks()