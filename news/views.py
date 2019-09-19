from django.shortcuts import render
from .models import news_model
from django.http import JsonResponse
import json
from rest_framework import generics
from .serializers import NewsSerializer
from django.shortcuts import get_object_or_404
# Create your views here.


# def get_content(request):
#     if request.method == 'GET':
#         model = news_model.show_manager.all()
#         serializer = NewsSerializer(model)
#     return JsonResponse({'data',serializer.data})


class NewsListView(generics.ListAPIView):
    queryset = news_model.show_manager.all()
    serializer_class = NewsSerializer


def image_detail(request, id, slug):
    image = get_object_or_404(news_model, id=id,slug=slug)
    return render(request, 'images/image/detail.html', {'section':'images','image':image})