from __future__ import absolute_import, unicode_literals

from celery import shared_task
from .status_checker import statuscheck


@shared_task
def get_streams():
    statuscheck.write_json()
    return('File written succesfully.')