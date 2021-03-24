from django.contrib import admin

from .models import *

# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'pub_date', 'image' ]


admin.site.register(Order)

