from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    # https://docs.djangoproject.com/zh-hans/3.2/ref/contrib/admin/
    list_display = ('username', 'email')
# Register your models here.
admin.site.register(User,UserAdmin)
