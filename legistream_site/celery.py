from __future__ import absolute_import, unicode_literals

import os
from . import settings

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'legistream_site.settings')

app = Celery('legistream_site')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'write_streams_bg': {
        'task': 'legistream.tasks.get_streams',
        'schedule': 60,

    }
}

app.autodiscover_tasks()