from django.urls import path, include
from . import views

app_name = 'home'

urlpatterns = [
    path('create/', views.image_create, name='create'),
]