from .views import UsernameCountView, EmailCountView, CreateUserAPIView
from django.urls import path
from django.conf.urls import url

urlpatterns = [
#     path('products', ProductViewSet.as_view({
#         'get': 'list',
#         'post': 'create'
#     })),
#     path('products/<str:pk>', ProductViewSet.as_view({
#         'get': 'retrieve',
#         'put': 'update',
#         'delete': 'destroy'
#     })),
#     url(r'^usernames/(?P<username>\w{3,20})/count/$',UsernameCountView.as_view()),
#     url(r'^mobiles/<str:email>/count/$',EmailCountView.as_view()),
    path('mobiles/<emailname>/count/', EmailCountView.as_view()),
    path('usernames/<username>/count/', UsernameCountView.as_view()),
    path('register/', CreateUserAPIView.as_view()),



]

# 路由router
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
# router.register('addresses',views.AddressViewSet,base_name='addresses')
urlpatterns += router.urls