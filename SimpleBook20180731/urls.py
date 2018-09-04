"""SimpleBook20180731 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
import json

from django.core.paginator import Paginator
from django.shortcuts import render

import xadmin as admin
from django.conf.urls import url,include

#主页请求的view函数
from art.models import Art, Category
from api import api_router


def toIndex(request):
    lu = request.session.get('login_user')
    if lu:
        login_user =json.loads(lu)
    cates = Category.objects.all()
    cateId = request.GET.get('cate')
    cateId = int(cateId) if cateId else 0
    arts = Art.objects.all() if cateId ==0 else Art.objects.filter(category_id=cateId)

    page = request.GET.get('page')
    page = int(page) if page else 1

    paginator = Paginator(arts,3)
    pager = paginator.page(page)

    return render(request,'index.html',locals())

urlpatterns = [
    url(r'^api/', include(api_router.urls)),
    #加上rest——framework授权管理的url
    url(r'^api-auth/',include('rest_framework.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^ueditor/', include('DjangoUeditor.urls')),
    url(r'^user/', include('user.urls')),
    url(r'^art/', include('art.urls')),
    url(r'^', toIndex),
]


