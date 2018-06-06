from django.contrib import admin

# Register your models here.
from . import models

@admin.register(models.Notification)
class NotificationAdmin(admin.ModelAdmin):

    list_display = (
        'creator',
        'to',
        'notification_type',
    )