from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings


@shared_task
def send_notification_email(email, subject, message):
    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        [email],
    )
