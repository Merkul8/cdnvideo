from celery import Celery
import os

# Настройки для celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cdnvideo.settings')

app = Celery('cdnvideo')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()