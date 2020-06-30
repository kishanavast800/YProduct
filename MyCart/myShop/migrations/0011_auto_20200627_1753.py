# Generated by Django 3.0.6 on 2020-06-27 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myShop', '0010_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='officestationary',
            name='products_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_id',
            field=models.DecimalField(decimal_places=2, max_digits=5, primary_key=True, serialize=False),
        ),
    ]
