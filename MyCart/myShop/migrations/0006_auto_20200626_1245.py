# Generated by Django 3.0.6 on 2020-06-26 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myShop', '0005_orders'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artiststationary',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='desktopstationary',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='electronicstationary',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='filling_and_storage_stationary',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='officestationary',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='paper_and_pad',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='printing_material',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='writtingstationary',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
