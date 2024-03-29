from django.db import models
from django import forms


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
        id_for_list = self.id
        return f"{id_for_list} {self.lists_name}"

    class Meta:
        verbose_name_plural = "Listy zakupów"


class ShoppingListForm(forms.ModelForm):
    class Meta:
        model = ShoppingLists
        fields = '__all__'
