from django.db import models


class Products(models.Model):
    product_name = models.CharField(max_length=15)
    quantity = models.PositiveSmallIntegerField(default=1)

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.id = None

    def __str__(self):
        return f"{self.id}, {self.product_name}"


class ShoppingLists(models.Model):
    products = models.ManyToManyField(Products)
    lists_name = models.CharField(max_length=30, default=id)

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.id = None

    def __str__(self):
        return f"{self.id} {self.lists_name}"
