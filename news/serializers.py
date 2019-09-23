from rest_framework import serializers
from .models import news_model


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = news_model
        fields = ['id', 'news_title', 'title_img', 'body', 'add_time', 'clicks',]