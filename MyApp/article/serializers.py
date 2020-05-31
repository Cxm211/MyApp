from rest_framework import serializers
from article.models import articleInfo

'''class articleSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return articleInfo.objects.create(validated_data)
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title',instance.title)
        instance.save()
        return instance'''


class articleSerializer(serializers.ModelSerializer):
    class Meta:
        model = articleInfo
        fields = ['id', 'title']


class commentSerializer(serializers.ModelSerializer):
    class Meta:
        model = articleInfo
        fields = ['id', 'title', 'comment']


class contentSerializer(serializers.ModelSerializer):
    class Meta:
        model = articleInfo
        fields = ['id', 'title', 'content']

