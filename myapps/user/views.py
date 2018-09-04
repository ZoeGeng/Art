import json
import os
import uuid

from django.contrib.auth.hashers import check_password
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.shortcuts import render, redirect
from django.http import JsonResponse

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from SimpleBook20180731 import settings
from user.forms import UserProfileForm
from user.models import UserProfile


def login(request):
    print('---*1')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        queryset = UserProfile.objects.filter(username=username)
        if queryset.exists():
            user = queryset.first()
            if check_password(password, user.password):
                login_user = json.dumps({
                    'id': user.id,
                    'name': user.username,
                    'photo': user.photo,
                })
                request.session['login_user'] = login_user
                print('---*2')
                return redirect('/')
            else:
                error_msg = '用户名或者口令不正确'
        else:
            error_msg = '用户%s不存在' % username

    return render(request, 'user/login.html',locals())


def regist(request):
    if request.method == 'GET':
        return render(request, 'user/regist.html')
    else:
        # 读取用户信息
        form = UserProfileForm(request.POST)
        print('--test1---')
        if form.is_valid():

            # form.photo = mvImageFromTmp(form.photo)

            user = form.save()
            request.session['login_user'] = json.dumps({'id':user.id,
                                                    'name': user.username,
                                                    'photo':user.photo})
            print('---test11')
            return redirect('/') #重定向到主页
        else:
            print('--test2---')
            errors_json = json.loads(form.errors.as_json())
            return render(request,
                          'user/regist.html',
                          locals()) #locals 收集当前函数内部的所有可用对象，生成字典

#实现文件上传的前端ajax接口
#@csrf_exempt:不验证csrf跨域问题
@csrf_exempt
def upload(request):
    print(request.method, request.POST)
    print(request.FILES)
    #获取上传的文件图片
    uImage:InMemoryUploadedFile = request.FILES.get('u_img')
    #生成新的文件名
    imgFileName = str(uuid.uuid4()).replace('-','') + os.path.splitext(uImage.name)[-1]
    #指定新文件保存位置
    imgFilePath = os.path.join(settings.MEDIA_ROOT,'user/'+imgFileName)
    with open(imgFilePath,'wb') as f:
        for chunk in uImage.chunks():
            f.write(chunk)
    return JsonResponse({'path':'/static/uploads/user/'+imgFileName,'status':'ok'})

def logout(request):
    del request.session['login_user']
    return redirect('/')