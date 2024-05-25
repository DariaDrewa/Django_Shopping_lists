from django.db import models
from django.urls import reverse


class Products(models.Model):
    product_name = models.CharField(max_length=30, verbose_name="Nazwa produktu", unique=True,
                                    error_messages={'unique': 'Taki produkt już istnieje!'})

    def __str__(self):
        return f"{self.product_name}"

    class Meta:
        verbose_name_plural = "Produkty"


class ShoppingLists(models.Model):
    lists_name = models.CharField(max_length=30, verbose_name="Nazwa listy", unique=True,
                                  error_messages={'unique': 'Lista o takiej nazwie już istnieje!'})
    products = models.ManyToManyField(Products, verbose_name="Produkty")

    def __str__(self):
        id_for_list = self.id
        return f"{id_for_list} {self.lists_name}"

    class Meta:
        verbose_name_plural = "Listy zakupów"

    def get_absolute_url(self):
        return reverse('details', args=[str(self.id)])
