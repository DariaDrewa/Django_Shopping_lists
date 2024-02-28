from django.db import models


class Products(models.Model):
    product_name = models.CharField(max_length=15)
    quantity = models.IntegerField(null=True)
