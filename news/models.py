from django.db import models
from tinymce.models import HTMLField
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.


class ShowManager(models.Manager):
    def get_queryset(self):
        return super(ShowManager, self).get_queryset().filter(is_show=True, is_delete=False)


class news_model(models.Model):
    news_title = models.CharField(max_length=50, verbose_name='新闻标题')  # 标题
    # body = models.TextField(verbose_name='新闻内容')  # 内容
    body = RichTextUploadingField(config_name='my_config')
    title_img = models.ImageField(upload_to='news/', verbose_name='标题图片')  # 图片路径
    body_img_1 = models.ImageField(upload_to='news/', verbose_name='内容图片1', blank=True)  # 图片路径
    body_img_2 = models.ImageField(upload_to='news/', verbose_name='内容图片2', blank=True)  # 图片路径
    body_img_3 = models.ImageField(upload_to='news/', verbose_name='内容图片3', blank=True)  # 图片路径
    add_time = models.DateTimeField(verbose_name='添加时间')  # 添加时间
    clicks = models.IntegerField(verbose_name='点击数量', blank=True, null=True)  # 点击数量
    is_show = models.BooleanField(verbose_name='是否显示')  # 是否显示
    is_delete = models.BooleanField(verbose_name='假删除')  # 假删除
    class Meta:
        verbose_name_plural = '新闻管理'
        ordering = ('-add_time',)

    objects = models.Manager()  # 默认管理器
    show_manager = ShowManager()

    def profile(self):
        """
        判断字段过长，则截取部分字段
        :return:
        """
        if len(str(self.body))>50:
            return '{}...'.format(str(self.body)[0:50])
        else:
            return str(self.body)

    profile.short_description = '新闻内容'


class GoodsInfo(models.Model):
    gcontent = HTMLField()

class NewsBody(models.Model):
    title = models.CharField(max_length=254, unique=True)
    # 博客的内容为 RichTextField 对象
    body = RichTextField()

    def __str__(self):
        return self.title
