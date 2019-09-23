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
