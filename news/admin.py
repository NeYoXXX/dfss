from django.contrib import admin
from .models import news_model, GoodsInfo, NewsBody
# Register your models here.

@admin.register(news_model)
class NewsModelAdmin(admin.ModelAdmin):
    list_display = ('news_title', 'profile', 'title_img', 'body_img_1', 'body_img_2', 'body_img_3', 'add_time', 'clicks',
                    'is_show', 'is_delete')  # 后台显示的字段
    list_filter = ('news_title', 'clicks', 'add_time', )  # 后台管理右侧边栏用于筛选结果
    search_fields = ('news_title', 'body',)
    date_hierarchy = 'add_time'  # 在搜索栏的下方，出现了时间层级导航条
    ordering = ('add_time', 'is_show',)  # 默认通过Status和Publish字段进行排序
    list_per_page = 10  # 每页中显示多少条数据


@admin.register(GoodsInfo)
class GoodsInfoAdmin(admin.ModelAdmin):
    list_display = ['id']


#注册该模型
@admin.register(NewsBody)
class BlogAdmin(admin.ModelAdmin):
    # 列表页面显示字段
    list_display = ['title', 'body']