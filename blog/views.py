from django.shortcuts import render, HttpResponse
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import random


# Create your views here.


def index(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'login.html')


# 生成验证码图片
def get_valid_img(request):
    # 生成RGB三原色代码
    def get_random_color():
        return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    # 生成纯色图片
    image = Image.new("RGB", (250, 40), get_random_color())
    # 生产五个随机字符串
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("static/font/kumo.ttf", size=32)
    temp = []
    for i in range(5):
        random_num = str(random.randint(0, 9))
        random_low_alpha = chr(random.randint(97, 122))
        random_upper_alpha = chr(random.randint(65, 90))
        random_char = random.choice([random_num, random_low_alpha, random_upper_alpha])
        draw.text((24 + i * 36, 0), random_char, get_random_color(), font=font)
        # 保存随机字符
        temp.append(random_char)
    # 写入内存
    f = BytesIO()
    image.save(f, "png")
    data = f.getvalue()
    f.close()

    valid_str = "".join(temp)
    print("valid_str", valid_str)
    request.session["valid_str"] = valid_str
    return HttpResponse(data)
