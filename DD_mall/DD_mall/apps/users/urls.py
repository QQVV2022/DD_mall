from .views import UsernameCountView, EmailCountView, ImagecodeView, EmailcodeView, CreateUserAPIView
from django.urls import path

urlpatterns = [
    path('mobiles/<emailname>/count/', EmailCountView.as_view()),
    path('usernames/<username>/count/', UsernameCountView.as_view()),
    path('image_codes/<image_code_id>/', ImagecodeView.as_view()),
    path('sms_codes/<email>/', EmailcodeView.as_view()),
    path('register/', CreateUserAPIView.as_view()),

]

