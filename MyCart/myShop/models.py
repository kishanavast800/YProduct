from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256, default="")
    short_description = models.CharField(max_length=100, default="")
    description = models.CharField(max_length=5000, default="")
    category = models.CharField(max_length=100, default="")
    secondary_category = models.CharField(max_length=500, default="")
    image1 = models.ImageField(upload_to="myShop/images", default="")
    image2 = models.ImageField(upload_to="myShop/images", default="")
    image3 = models.ImageField(upload_to="myShop/images", default="")
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name
class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200,default="")
    phone = models.CharField(max_length=200, default="")
    desc = models.CharField(max_length=50000,default="")

class Orders(models.Model):
    order_id = models.AutoField(primary_key = True)
    items_json = models.CharField(max_length=5000)
    name = models.CharField(max_length=90)
    amount = models.IntegerField(default=0)
    email = models.CharField(max_length=120)
    address = models.CharField(max_length=50000)
    city = models.CharField(max_length=120)
    state = models.CharField(max_length=120)
    zip_code = models.CharField(max_length=120)
    phone = models.CharField(max_length=120 , default="")
class Request(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200, default="")
    phone = models.CharField(max_length=200, default="")
    desc = models.CharField(max_length=50000, default="")
    image = models.ImageField(upload_to="myShop/images/", default="")
