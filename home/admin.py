from django.contrib import admin
from .models import poll_img_model, middle_model, half_bottom_model
# Register your models here.

@admin.register(poll_img_model)
class poll_img_model_admin(admin.ModelAdmin):
    list_display = ['label_p_big', 'label_p_little', 'label_img', 'label_p_add_time', 'is_show', 'is_delete']


@admin.register(middle_model)
class middle_model_admin(admin.ModelAdmin):
    list_display = ['label_p_big', 'label_p_little', 'label_img', 'label_p_add_time', 'is_show', 'is_delete']


@admin.register(half_bottom_model)
class half_bottom_model_admin(admin.ModelAdmin):
    list_display = ['label_p_big', 'label_p_little', 'label_img', 'label_p_add_time', 'is_show', 'is_delete']