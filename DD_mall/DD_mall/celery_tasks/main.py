from celery import Celery
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DD_mall.settings')

app = Celery('ddmall')  # creat Celery app
app.config_from_object('celery_tasks.config')  # config the broker

#  register celery taskcd ..

app.autodiscover_tasks(['celery_tasks.email_task'])