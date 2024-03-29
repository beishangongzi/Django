from django.contrib import admin
from myapp import models

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ("nickName", "message", "enabled", "pub_time")
    ordering = ("-pub_time",)

admin.site.register(models.Mood)
admin.site.register(models.Post, PostAdmin)