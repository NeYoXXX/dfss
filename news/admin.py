from django.contrib import admin
from .models import news_model
# Register your models here.

@admin.register(news_model)
class NewsModelAdmin(admin.ModelAdmin):
    list_display = ('news_title', 'body', 'title_img', 'body_img_1', 'body_img_2', 'body_img_3', 'add_time', 'clicks',
                    'is_show', 'is_delete')  # 后台显示的字段
    list_filter = ('news_title', 'clicks', 'add_time', )  # 后台管理右侧边栏用于筛选结果
    search_fields = ('news_title', 'body',)
    date_hierarchy = 'add_time'  # 在搜索栏的下方，出现了时间层级导航条
    ordering = ('add_time', 'is_show',)  # 默认通过Status和Publish字段进行排序
