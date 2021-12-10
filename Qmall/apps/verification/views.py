from django.shortcuts import render
from django.http import JsonResponse
from  django.views import View
# from .my_captcha import FormWithCaptcha

# Create your views here.
class ReCaptCha(View):
    def get(self,request):

        return JsonResponse(request, context)