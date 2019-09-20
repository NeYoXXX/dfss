from .models import news_model
from rest_framework import generics
from .serializers import NewsSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.


class NewsListView(generics.ListAPIView):
    queryset = news_model.show_manager.all()
    serializer_class = NewsSerializer


class NewsDetail(APIView):
    def get(self,request):
        id = request.GET.get('id')
        model = news_model.show_manager.get(id=id)
        serializer = NewsSerializer(model)
        return Response(serializer.data)

