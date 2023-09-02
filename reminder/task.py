from celery import shared_task
from az.celery import app
import datetime
from reminder.models import reminder
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def send_reminder_email():
    try:
        remObj = reminder.objects.filter(is_mail=True)
        for obj in remObj:
            if datetime.datetime.now().date() == obj.date_of_action:
                print("sameeeeeeeeee from task")
                subject = obj.title
                message = obj.description 
                recipient_list=obj.mail
                email_from=settings.EMAIL_HOST_USER
                send_mail(subject, message, email_from, [recipient_list], fail_silently=False)
                print("it is today")
            else:
                print("Not todayyyyy from taskk")
    except Exception as e:
        print(e)