from django.shortcuts import render
from django.http import JsonResponse
from .models import user
# Create your views here.


def index(request):
    return render(request, 'index.html')


def login(request):
    username = request.GET.get('username')
    password = request.GET.get('password')
# 登录判断
    usr = user.objects.filter(
        username=username) .first()  # queryset,找不到返回None
    code = 1
    msg = "登陆成功"
    if usr == None:  # 不存在
        code = 0
        msg = "用户不存在!"
    else:
        if usr.password != password:  # 密码错误
            code = -1
            msg = "密码错误"

    res = {
        "code": code,  # 状态编码
        "msg": msg
    }
    return JsonResponse(res, safe=False)
    # return render(request, 'home.html')


def home(request):
    return render(request, 'home.html')
