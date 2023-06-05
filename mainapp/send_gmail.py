from django.core.mail import EmailMessage
from django.conf import settings
from celery import shared_task

@shared_task
def send_msg(email):
    mail = EmailMessage(
        'Hello',
        'Привет, регистрация прошла успешно',
        settings.EMAIL_HOST_USER,
        [email]
    )

    mail.attach_file('mainapp/text.txt')                              # внутри скобки нужно указать путь файла
    mail.send()