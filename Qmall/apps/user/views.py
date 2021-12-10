from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from django.contrib.auth import login
import re
import json
from apps.user.models import User


# Create your views here.
class UserNameCheck(View):
    def get(self, request, username):
        print("User name check")
        if (not re.match(r'^[a-zA-Z0-9_-]{5,20}$', username)) and  re.match('^[0-9]+$', username):
            return JsonResponse({"code":0, "count":100, "error_name_message":"The length of user name is 5-20 and cannot be all number!"})
        if_user_exist = User.objects.filter(username=username).exists()
        if if_user_exist:
            return JsonResponse({"code": 0, "count": 1, "error_name_message": "User name is existed!"})
        else:
            return JsonResponse({"code": 0, "count": 0, "error_name_message": "Success!"})



class EmailCheck(View):
    def get(self, request, email):
        print("email check")
        if not re.match(r'^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$', email):
            return JsonResponse({"code":0, "count":100, "error_email_message":"Email Address is incorrect!!"})
        if_user_exist = User.objects.filter(email=email).exists()
        print("if user exist", if_user_exist)
        if if_user_exist:
            return JsonResponse({"code": 0, "count": 1, "error_email_message": "Email is existed!"})
        else:
            return JsonResponse({"code": 0, "count": 0, "error_email_message": "Success!"})


class Register(View):
    def post(self, request):
        # 1  check the request data,
        # 2 if 2 psw the same,
        # 3 check the email name if existed,
        # 4 check if agreement checked,
        # 5 send activate email by celery
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)

        username = body.get("username")
        password = body.get("password")
        password2 = body.get("password2")
        email = body.get("email")
        # sms_code = body.get("sms_code")
        allow = body.get("allow")

        print(username,password,password2,email,allow)

        if not all([username,password,password2,email,allow]):
            return JsonResponse({"code":400, "errmsg":"Please fulfill all data!!!"})

        if (not re.match(r'^[a-zA-Z0-9_-]{5,20}$', username)) and  re.match('^[0-9]+$', username):
            return JsonResponse({"code":0, "count":100, "message":"The length of user name is 5-20 and cannot be all number!"})
        if_user_exist = User.objects.filter(username=username).exists()
        if if_user_exist:
            return JsonResponse({"code": 0, "count": 1, "message": "User name is existed!"})


        if password != password2:
            return JsonResponse({"code":400, "errmsg":"Passwords are not match!!!"})
        if len(password) < 8 or len(password) > 20:
            return JsonResponse({"code":400, "errmsg":"Password's length should between 8 and 20!!!"})

        if not re.match(r'\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$', email):
            return JsonResponse({"code":400,  "message":"Email address is incorrect!!!"})

        user = User.objects.create_user(username=username,password=password,email=email)  # password is encrypted!
        login(request, user)

        return JsonResponse({"code":0, "errmsg":"Log in Seccussfully!"})




