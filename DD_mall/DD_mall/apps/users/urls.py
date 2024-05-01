from .views import UsernameCountView, EmailCountView, ImagecodeView, CreateUserAPIView
from django.urls import path
from django.conf.urls import url

urlpatterns = [
    path('mobiles/<emailname>/count/', EmailCountView.as_view()),
    path('usernames/<username>/count/', UsernameCountView.as_view()),
    path('image_codes/<image_code_id>/', ImagecodeView.as_view()),
    path('register/', CreateUserAPIView.as_view()),

]

# 路由router
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
# router.register('addresses',views.AddressViewSet,base_name='addresses')
urlpatterns += router.urls