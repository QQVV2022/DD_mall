from celery_tasks.main import app
from django.conf import settings
from django.core.mail import send_mail
@app.task(name='send_email_code')
def send_email_code(to_email, text):
    subject = "DD_MAll Verification Code"
    html_message = f"Your verification code is {text}"
    send_mail(subject, html_message, settings.EMAIL_HOST_USER, html_message=html_message)