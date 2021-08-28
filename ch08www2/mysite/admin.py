from django.contrib import admin
from . import models

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ("nickName", "message", "enabled", "pubDate")
    ordering = ("-pubDate",)

admin.site.register(models.Mood)
admin.site.register(models.Post, PostAdmin)

