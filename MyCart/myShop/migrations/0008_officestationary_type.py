# Generated by Django 3.0.6 on 2020-06-26 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myShop', '0007_auto_20200626_1621'),
    ]

    operations = [
        migrations.AddField(
            model_name='officestationary',
            name='type',
            field=models.CharField(default='', max_length=500),
        ),
    ]