from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

class ShowManager(models.Manager):
    def get_queryset(self):
        return super(ShowManager, self).get_queryset().filter(is_show=True, is_delete=False)


class CaseModel(models.Model):
    title = models.CharField(max_length=50, verbose_name='案例标题')
    title_img = models.ImageField(upload_to='news/', verbose_name='标题图片')
    introduce = models.TextField(max_length=200, verbose_name='简介')
    body = RichTextUploadingField(config_name='my_config', verbose_name='内容')
    add_time = models.DateTimeField(verbose_name='添加时间')  # 添加时间
    clicks = models.IntegerField(verbose_name='点击数量', blank=True, null=True)  # 点击数量
    is_show = models.BooleanField(verbose_name='是否显示')  # 是否显示
    is_delete = models.BooleanField(verbose_name='假删除')  # 假删除

    class Meta:
        verbose_name_plural = '案例管理'
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

    profile.short_description = '内容'