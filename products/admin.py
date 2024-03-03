from django.contrib import admin
from .models import Products, ShoppingLists


class ProductsAdmin(admin.ModelAdmin):
    list_display = ("product_name", "quantity")


class ShoppingListsAdmin(admin.ModelAdmin):
    list_display = (id, "lists_name")


admin.site.register(Products, ProductsAdmin)
admin.site.register(ShoppingLists, ShoppingListsAdmin)

