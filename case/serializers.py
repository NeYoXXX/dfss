from rest_framework import serializers
from .models import CaseModel


class CaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaseModel
        fields = ['id', 'title', 'title_img', 'body', 'introduce', 'add_time', 'clicks',]