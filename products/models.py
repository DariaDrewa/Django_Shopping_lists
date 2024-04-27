from django.db import models


class Products(models.Model):
    product_name = models.CharField(max_length=15, verbose_name="Nazwa produktu")

    def __str__(self):
        return f"{self.product_name}"

    class Meta:
        verbose_name_plural = "Produkty"


class ShoppingLists(models.Model):
    lists_name = models.CharField(max_length=30, verbose_name="Nazwa listy")
    products = models.ManyToManyField(Products, verbose_name="Produkty")

    def __str__(self):
        id_for_list = self.id
        return f"{id_for_list} {self.lists_name}"

    class Meta:
        verbose_name_plural = "Listy zakupów"



