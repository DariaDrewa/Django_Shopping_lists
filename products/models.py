from django.db import models


class Products(models.Model):
    product_name = models.CharField(max_length=15)
    quantity = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.product_name} {self.quantity}"

