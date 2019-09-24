from .models import CaseModel
from rest_framework import generics
from .serializers import CaseSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.


class CaseListView(generics.ListAPIView):
    queryset = CaseModel.show_manager.all()
    serializer_class = CaseSerializer


class CaseDetail(APIView):
    def get(self,request):
        id = request.GET.get('id')
        model = CaseModel.show_manager.get(id=id)
        serializer = CaseSerializer(model)
        return Response(serializer.data)
