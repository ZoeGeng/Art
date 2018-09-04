import json

from django.views.decorators.cache import cache_page

from utils import redis_cache

from django.http import JsonResponse
from django.shortcuts import render

from art import tasks
from art.models import Art

@cache_page(10)
def show(request, artId):
    # 读取当前用户信息
    if request.session.get('login_user'):
        login_user = json.loads(request.session.get('login_user'))
    # 查看指定的文章
    art = Art.objects.get(id=artId)
    redis_cache.zincrby('rankTop', artId)
    rankArtTop = listRankTop(5)
    return render(request, 'art/show.html', locals())

def listRankTop(top):
    rank_ids = redis_cache.zrevrange('rankTop',0,top-1,withscores=True)
    ids = [int(id.decode()) for id, score in rank_ids]

    rank_arts = Art.objects.in_bulk(ids)
    return [(rank_arts.get(int(id.decode())), int(score)) for id, score in rank_ids]



def advance(request, artId):
    login_user = request.session.get('login_user')
    #抢读
    if not login_user:
        return JsonResponse({'status':101,
                             'msg':'亲，请先登录'})


    login_user = json.loads(login_user)
    user_id = login_user.get('id')
    if redis_cache.hexists('AdvanceArt', user_id):
        return JsonResponse({'status': 205,
                             'msg':'亲，给别人点机会吧'})
    tasks.advanceArt.delay(artId,user_id)
    return JsonResponse({'status':201,'msg':'正在抢读，请稍等'})

def queryAdvance(request, artId):
    login_user = request.session.get('login_user')
    if not login_user:
        return JsonResponse({'status':101,
                             'msg':'亲，请先登录'})
    user_id = json.loads(login_user).get('id')
    artId = redis_cache.hget('AdvanceArt',user_id)
    print(1)
    if artId:
        art = Art.objects.get(id=artId.decode())
        print(2)
        return JsonResponse({
            'status':200,
            'msg':'恭喜,抢读%s成功'%art.title
        })
    else:
        if redis_cache.hlen('AdvanceArt') < 5:
            return JsonResponse({'status':202,'msg':'正在抢读，请稍等'})
        else:
            return JsonResponse({'status':203,'msg':'祝下次好运'})

