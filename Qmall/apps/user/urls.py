from django.urls import path, include
from apps.user.views import UserNameCheck, EmailCheck, Register

urlpatterns = [
    path('usernames/<username>/count/', UserNameCheck.as_view(), name="usernamecheck"),
    path('email/<email>/count/', EmailCheck.as_view(), name="emailcheck"),
    path('register/', Register.as_view(), name="register")





]