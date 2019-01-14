from django.shortcuts import render, HttpResponse


# Create your views here.


def index(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')


# 生成验证码图片
def get_valid_img(request):
    with open("/blog/1.jpg", 'rb') as f:
        data = f.read()

    return HttpResponse(data)
