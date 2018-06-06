from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'file',
        'location',
        'caption',
        'creator',
        'created_at',
        'updated_at',
    )

    list_filter = (
        'location',
        'creator',
    )

    list_display_links = (
        'location',
    )

    search_fields = (
        'location',
        'caption',
    )

@admin.register(models.Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = (
        'creator',
        'image',
    )
    

@admin.register(models.Comment)
class CommnetAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'message',
        'creator',
        'image',
        'created_at',
        'updated_at'
    )

