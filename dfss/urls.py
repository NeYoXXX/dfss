"""dfss1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import settings
from django.conf.urls import static
urlpatterns = [
    path('api/admin/', admin.site.urls),
    path('api/home/', include('home.urls',namespace='home')),
    path('api/news/', include('news.urls',namespace='news')),
    path('api/case/', include('case.urls',namespace='case')),
    path('api/ckeditor/', include('ckeditor_uploader.urls')),
]

# 线下测试使用
urlpatterns += static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
