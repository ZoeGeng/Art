from rest_framework import serializers,viewsets

from art.models import Art


class ArtSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Art
        fields = ['id','title','author','cover','publish_time','category']
#将分类显示试图注册到API路由中
class ArtViewSet(viewsets.ModelViewSet):
    queryset = Art.objects.all()
    serializer_class = ArtSerializer