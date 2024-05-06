from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User
from .serializers import CreateUserSerializer

import random
from django_redis import get_redis_connection
from django.http import HttpResponse

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
        redis_conn.setex(f"image_code_{image_code_id}", 300, text.lower())
        return HttpResponse(image, content_type="image/jpeg")


class EmailcodeView(APIView):
    def get(self, request, email):
        '''
        verify image code if correct, if yes, send email verification code, else send error message
        '''
        count = User.objects.filter(email=email).count()
        if count > 0:
            return Response({'errmsg': 'Email existed!'})

        redis_conn = get_redis_connection("verify_codes")

        img_code_id = request.GET.get("image_code_id")
        img_code = request.GET.get("image_code")
        redis_img_code = redis_conn.get(f"image_code_{img_code_id}")
        if not img_code or not redis_img_code or redis_img_code.decode() != img_code.lower():
            return Response({'message': 'Image code expired or incorrect!'})
        redis_conn.delete(f"image_code_{img_code_id}")

        code = "".join([str(random.randint(0, 9)) for i in range(6)])
        email = email.lower()
        redis_conn.setex(f"code_{email}", 6000, code)

        from celery_tasks.email_task.tasks import send_email_code
        send_email_code.delay(email, code)
        return Response({'code': 200, 'message': 'ok'})

class CreateUserAPIView(APIView):
    def post(self, request):
        print('**', request.data)
        serializer = CreateUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'errmsg': 'ok', 'code': 0}, status=status.HTTP_201_CREATED)  # fron end code == 0 means success in Line 223

