import builtins
from django.db import models


class Products(models.Model):
    product_name = models.CharField(max_length=15)
    quantity = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return f"{self.id} - {self.product_name}"

    class Meta:
        verbose_name_plural = "Produkty"

class ShoppingLists(models.Model):
    lists_name = models.CharField(max_length=30)
    products = models.ManyToManyField(Products)

    def __str__(self):
        return f"{self.lists_name}"

    class Meta:
        verbose_name_plural = "Listy zakupów"