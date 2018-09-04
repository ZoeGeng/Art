from SimpleBook20180731.celery import app
from utils import redis_cache

@app.task
def advanceArt(artId, userId):
    #抢读
    print('用户',userId,'正在抢读',artId)
    if redis_cache.hlen('AdvanceArt') >= 5:
        return artId + '抢读失败'
    redis_cache.hset('AdvanceArt',userId,artId)
    return artId + '抢读成功!'
@app.task
def sendEmailLog():
    #读取指定日志文件的内容，并发送给管理员
    print('已发送邮件')
    return '日志邮箱已发送'
