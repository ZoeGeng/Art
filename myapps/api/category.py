



#声明分类显示视图集
from rest_framework import serializers, viewsets

from api.art import ArtSerializer
from art.models import Category


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    add_time = serializers.DateTimeField(format='%Y-%m-%d')
    arts = serializers.StringRelatedField(many=True)
    #引入其他的序列化
    # arts = ArtSerializer(many=True,read_only=True)
    class Meta:
        model = Category
        # c=  Category()
        fields = ['id','name','add_time','arts']
#将分类显示试图注册到API路由中
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
