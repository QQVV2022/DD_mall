from celery import Celery

app = Celery('ddmall')  # creat Celery app
app.config_from_object('celery_tasks.config')  # config the broker

#  register celery task
app.autodiscover_tasks(['celery_tasks.email_task'])