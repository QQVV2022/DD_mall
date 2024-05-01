from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User
from .serializers import CreateUserSerializer

import re
from django_redis import get_redis_connection
from django.http import HttpResponse



# from .producer import publish
# from .serializers import User
# import random


# class ProductViewSet(viewsets.ViewSet):
#     def list(self, request):
#         products = Product.objects.all()
#         serializer = ProductSerializer(products, many=True)
#         return Response(serializer.data)
#
#     def create(self, request):
#         serializer = ProductSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         publish('product_created', serializer.data)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#
#     def retrieve(self, request, pk=None):
#         product = Product.objects.get(id=pk)
#         serializer = ProductSerializer(product)
#         return Response(serializer.data)
#
#     def update(self, request, pk=None):
#         product = Product.objects.get(id=pk)
#         serializer = ProductSerializer(instance=product, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         publish('product_updated', serializer.data)
#         return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
#
#     def destroy(self, request, pk=None):
#         product = Product.objects.get(id=pk)
#         product.delete()
#         publish('product_deleted', pk)
#         return Response(status=status.HTTP_204_NO_CONTENT)

class UsernameCountView(APIView):
    def get(self, request, username):
        '''
            Verify if username meets the requirements.
            get username count in db, if it is 0, then meets, else not
        '''
        count = User.objects.filter(username=username).count()
        return Response({'count': count, 'username': username, 'errmsg': 'ok'})

class EmailCountView(APIView):
    def get(self, request, emailname):
        '''
            When register, to verify if email address existed in db, if it is 0, then meets, else not.
        '''
        count = User.objects.filter(email=emailname).count()
        return Response({'count': count, 'email': emailname, 'errmsg': 'ok'})


class ImagecodeView(APIView):
    '''
    image code
    '''

    def get(self, request, image_code_id):
        from utils.captcha.captcha import captcha
        _, text, image = captcha.generate_captcha()
        redis_conn = get_redis_connection("verify_codes")
        redis_conn.setex(f"ImageCode_image_code_id", 300, text)
        return HttpResponse(image, content_type="image/jpeg")

class CreateUserAPIView(APIView):
    def post(self, request):
        serializer = CreateUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'errmsg': 'ok', 'code': 0}, status=status.HTTP_201_CREATED)  # fron end code == 0 means success in Line 223

