from celery import shared_task
from django.core.mail import send_mail

from time import sleep


@shared_task
def send_email_task():
    sleep(8)
    send_mail(
        'Subject of the letter',
        'Body of the letter',
        'sender_name@example.com',
        ['address1@example.com', 'address2@example.com']
    )
