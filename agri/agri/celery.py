from __future__ import absolute_import, unicode_literals

import os
from celery import Celery
from django.conf import settings

# set the default Django settings module for the 'celery' program.

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'agri.settings')

broker_url = ':'.join(['amqp', f'//{settings.RABBITMQ_DEFAULT_USER}', f'{settings.RABBITMQ_DEFAULT_PASS}@rabbitmq', '5672'])
celery_app = Celery('agri', broker=broker_url)

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
celery_app.config_from_object('django.conf:settings', namespace='CELERY')
