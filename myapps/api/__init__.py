from rest_framework import routers

from api.art import ArtViewSet
from api.category import CategoryViewSet

#创建一个api路由对象
api_router = routers.DefaultRouter()

api_router.register(r'cate', CategoryViewSet)
api_router.register(r'art', ArtViewSet)
