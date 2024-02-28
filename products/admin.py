from django.contrib import admin
from .models import Products


class ProductsAdmin(admin.ModelAdmin):
    list_display = ("product_name", "quantity")


admin.site.register(Products, ProductsAdmin)


