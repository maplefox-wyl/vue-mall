import time

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import *
from django.http import HttpRequest, JsonResponse, HttpResponse
import json

url = 'https:127.0.0.1'
# 测试
def test(req):
    return request.put(url,headers,data)


# 注册
def user(request):
    # now = int(time.time())  # 1533952277
    # timeArray = time.localtime(now)
    # time_now = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    if request.method == "GET":
        return render(request, "user.html", locals())
    elif request.method == "POST":
        username = request.POST["username"]
        print(username)
        phone = request.POST["phone"]
        email = request.POST["mail"]
        password_1 = request.POST["password1"]
        password_2 = request.POST["password2"]
        if not username:
            result = {'code': 203, 'error': '请填写用户账号 !'}
            return JsonResponse(result)
        if not phone:
            result = {'code': 204, 'error': '请填写手机号 !'}
            return JsonResponse(result)

        if not email:
            result = {'code': 205, 'error': '请填写Email !'}
            return JsonResponse(result)

        if not password_1 or not password_2:
            result = {'code': 206, 'error': '请填写密码 !'}
            return JsonResponse(result)

        if password_1 != password_2:
            result = {'code': 207, 'error': '请填写正确密码 !'}
            return JsonResponse(result)

        # 检查用户名是否存在
        old_user = User.objects.filter(username=username)
        if old_user:
            result = {'code': 208, 'error': '该用户已经存在 !!! '}
            return JsonResponse(result)
        try:
            User.objects.create(username=username, phone=phone, email=email, password=password_1)
        except Exception as e:
            print('注册失败')
            result = {'code': 500, 'error': '服务器繁忙 !'}
            return JsonResponse(result)
        result = {'code': 200, 'username': username}
        return render(request, "index.html", locals())


def login(request):
    pass
