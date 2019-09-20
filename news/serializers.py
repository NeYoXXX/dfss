from rest_framework import serializers
from .models import news_model


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = news_model
        fields = ['id', 'news_title', 'body', 'title_img', 'body_img_1', 'body_img_2', 'body_img_3', 'add_time', 'clicks',]