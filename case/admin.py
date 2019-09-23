from django.contrib import admin
from .models import CaseModel
# Register your models here.

@admin.register(CaseModel)
class CaseModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'title_img', 'profile', 'add_time', 'clicks', 'is_show', 'is_delete')  # 后台显示的字段
    list_filter = ('title', 'clicks', 'add_time',)  # 后台管理右侧边栏用于筛选结果
    search_fields = ('title', 'profile',)
    date_hierarchy = 'add_time'  # 在搜索栏的下方，出现了时间层级导航条
    ordering = ('add_time', 'is_show',)  # 默认通过Status和Publish字段进行排序
    list_per_page = 10  # 每页中显示多少条数据