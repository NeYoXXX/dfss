from django.db import models


# Create your models here.


class ShowManager(models.Manager):
    def get_queryset(self):
        return super(ShowManager, self).get_queryset().filter(is_show=True, is_delete=False)


class news_model(models.Model):
    news_title = models.CharField(max_length=50)  # 标题
    body = models.TextField()  # 内容
    title_img = models.ImageField(upload_to='news/%Y/%m/%d')  # 图片路径
    body_img_1 = models.ImageField(upload_to='news/%Y/%m/%d')  # 图片路径
    body_img_2 = models.ImageField(upload_to='news/%Y/%m/%d')  # 图片路径
    body_img_3 = models.ImageField(upload_to='news/%Y/%m/%d')  # 图片路径
    add_time = models.DateTimeField()  # 添加时间
    clicks = models.IntegerField()  # 点击数量
    is_show = models.BooleanField()  # 是否显示
    is_delete = models.BooleanField()  # 假删除

    class Meta:
        ordering = ('-add_time',)

    objects = models.Manager()  # 默认管理器
    show_manager = ShowManager()

    # news_title.short_description = '标题'
    # body.short_description = '内容'
    # title_img.short_description = '标题图片'
    # body_img_1.short_description = '内容图片1'
    # body_img_2.short_description = '内容图片2'
    # body_img_3.short_description = '内容图片3'
    # add_time.short_description = '添加时间'
    # clicks.short_description = '阅读数量'
    # is_show.short_description = '是否显示'
    # is_delete.short_description = '是否删除'
