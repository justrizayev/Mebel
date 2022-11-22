from django.contrib import admin
from .models import *


# Register your models here.


class ProductImgInline(admin.StackedInline):
    model = ProductImg


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImgInline]


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)

