from django.contrib import admin

# Register your models here.
from myApp import models
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'pmodel',
        'nickName', 'price', 'year'
    ]
    search_fields = ('nickName', )
    ordering = ('-price', )
admin.site.register(models.Maker)
admin.site.register(models.PModel)
admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.PPhoto)
