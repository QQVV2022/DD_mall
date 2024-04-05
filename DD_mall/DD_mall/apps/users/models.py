from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    mobile = models.CharField(max_length=10, unique=True, verbose_name='mobile')

    class Meta:
        db_table = 'tb_user'
        verbose_name = 'USERS'
