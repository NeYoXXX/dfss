from django.shortcuts import render
from .models import news_model
from django.http import JsonResponse
# Create your views here.


def get_content(request):
    if request.method == 'GET':
        news_model.show_manager.all()
    return JsonResponse()