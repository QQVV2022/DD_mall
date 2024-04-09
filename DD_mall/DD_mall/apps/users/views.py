from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.users.models import User



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


class UserAPIView(APIView):
    def get(self, request, username):
        print('-------dd---')
        count = User.objects.filter(username=username).count()
        return Response({
            'code':count,
            'count': 22,
            'errmsg': 'ok'
        })
