from django.urls import path, include
from apps.user.views import UserNameCheck

urlpatterns = [
    path('usernames/<username>/count/', UserNameCheck.as_view(), name="usernamecheck"),
    path('usernames/<email>/count/', UserNameCheck.as_view(), name="emailcheck"),





]