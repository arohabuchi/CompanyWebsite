import os
from celery.schedules import crontab
from celery import Celery
from django.conf import settings

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'az.settings')

app = Celery('az')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'add-every-2-hour' :{
        'task':'send_reminder_email',
        'schedule':crontab(minute='*/1'),
    }
}


@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')