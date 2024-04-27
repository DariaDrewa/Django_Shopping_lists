# Generated by Django 5.0.2 on 2024-04-27 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_products_quantity_shoppinglists'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='products',
            options={'verbose_name_plural': 'Produkty'},
        ),
        migrations.AlterModelOptions(
            name='shoppinglists',
            options={'verbose_name_plural': 'Listy zakupów'},
        ),
        migrations.RemoveField(
            model_name='products',
            name='quantity',
        ),
        migrations.AlterField(
            model_name='products',
            name='product_name',
            field=models.CharField(max_length=15, verbose_name='Nazwa produktu'),
        ),
        migrations.AlterField(
            model_name='shoppinglists',
            name='lists_name',
            field=models.CharField(max_length=30, verbose_name='Nazwa listy'),
        ),
        migrations.AlterField(
            model_name='shoppinglists',
            name='products',
            field=models.ManyToManyField(to='products.products', verbose_name='Produkty'),
        ),
    ]
