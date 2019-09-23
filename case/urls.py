from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.CaseListView.as_view(), name=''),
    # path('details/', views.NewsDetail.as_view()),
]