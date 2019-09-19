from django.urls import path, include
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.NewsListView.as_view(), name=''),
]