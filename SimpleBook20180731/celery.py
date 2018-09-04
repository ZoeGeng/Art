
from __future__ import absolute_import,unicode_literals

import os

import django.conf
from celery import Celery
from django.conf import settings

#设置环境变量
os.environ.setdefault('DJANGO_SETTINGS_MODULE','SimpleBook20180731.settings')
app = Celery('artCelery')
app.config_from_object('django.conf:settings')

#自动查找当前项目中的Celery的task(异步函数)
app.autodiscover_tasks(lambda :settings.INSTALLED_APPS)


