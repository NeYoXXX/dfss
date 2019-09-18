from django.db import models

# Create your models here.

class poll_img_model(models.Model):
    '''
    首页轮询图片
    '''
    label_p_big = models.CharField(max_length = 10)  #大标题
    label_p_little = models.CharField(max_length = 100) #小标题
    label_img = models.ImageField(upload_to='images/%Y/%m/%d')  #图片路径
    label_p_add_time = models.DateTimeField()  #添加时间
    is_show = models.BooleanField()  #是否显示
    is_delete = models.BooleanField()  #假删除

class middle_model(models.Model):
    '''
    首页中间部分介绍
    '''
    label_p_big = models.CharField(max_length = 10)  #大标题
    label_p_little = models.CharField(max_length = 100) #小标题
    label_img = models.ImageField(upload_to='images/%Y/%m/%d')  #图片路径
    label_p_add_time = models.DateTimeField()  #添加时间
    is_show = models.BooleanField()  #是否显示
    is_delete = models.BooleanField()  #假删除

class half_bottom_model(models.Model):
    '''
    首页下部分介绍
    '''
    label_p_big = models.CharField(max_length = 10)  #大标题
    label_p_little = models.CharField(max_length = 100) #小标题
    label_img = models.ImageField(upload_to='images/%Y/%m/%d')  #图片路径
    label_p_add_time = models.DateTimeField()  #添加时间
    is_show = models.BooleanField()  #是否显示
    is_delete = models.BooleanField()  #假删除