import logging
#配置root日志记录器
logging.getLogger().setLevel(logging.INFO)

#日志格式化
formatter = '[%(asctime)s->%(module)s->%(funcName)s at %(lineno)s]->%(message)s'
#设置root基本配置
logging.basicConfig(format=formatter,
                    datefmt='%Y-%m-%d %H:%M:%S')





