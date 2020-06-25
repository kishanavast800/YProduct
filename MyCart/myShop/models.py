from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=100,default="")
    pub_date = models.DateField()
    image = models.ImageField(upload_to="myShop/images", default="")
    def __str__(self):
        return self.product_name

class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200,default="")
    phone = models.CharField(max_length=200, default="")
    desc = models.CharField(max_length=50000,default="")

class Officestationary(models.Model):
    products_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256,default="")
    short_description = models.CharField(max_length=100, default="")
    description = models.CharField(max_length=256,default="")
    category = models.CharField(max_length=100,default="")
    image1 = models.ImageField(upload_to="myShop/images", default="")
    image2 = models.ImageField(upload_to="myShop/images", default="")
    image3 = models.ImageField(upload_to="myShop/images", default="")
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    def __str__(self):
        return self.name

class Desktopstationary(models.Model):
    products_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256,default="")
    short_description = models.CharField(max_length=100, default="")
    description = models.CharField(max_length=256,default="")
    category = models.CharField(max_length=100,default="")
    image1 = models.ImageField(upload_to="myShop/images", default="")
    image2 = models.ImageField(upload_to="myShop/images", default="")
    image3 = models.ImageField(upload_to="myShop/images", default="")
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    def __str__(self):
        return self.name

class Artiststationary(models.Model):
    products_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256,default="")
    short_description = models.CharField(max_length=100, default="")
    description = models.CharField(max_length=256,default="")
    category = models.CharField(max_length=100,default="")
    image1 = models.ImageField(upload_to="myShop/images", default="")
    image2 = models.ImageField(upload_to="myShop/images", default="")
    image3 = models.ImageField(upload_to="myShop/images", default="")
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    def __str__(self):
        return self.name

class Writtingstationary(models.Model):
    products_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256,default="")
    short_description = models.CharField(max_length=100, default="")
    description = models.CharField(max_length=256,default="")
    category = models.CharField(max_length=100,default="")
    image1 = models.ImageField(upload_to="myShop/images", default="")
    image2 = models.ImageField(upload_to="myShop/images", default="")
    image3 = models.ImageField(upload_to="myShop/images", default="")
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    def __str__(self):
        return self.name

class Paper_and_pad(models.Model):
    products_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256,default="")
    short_description = models.CharField(max_length=100, default="")
    description = models.CharField(max_length=256,default="")
    category = models.CharField(max_length=100,default="")
    image1 = models.ImageField(upload_to="myShop/images", default="")
    image2 = models.ImageField(upload_to="myShop/images", default="")
    image3 = models.ImageField(upload_to="myShop/images", default="")
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    def __str__(self):
        return self.name

class Filling_and_storage_stationary(models.Model):
    products_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256,default="")
    short_description = models.CharField(max_length=100, default="")
    description = models.CharField(max_length=256,default="")
    category = models.CharField(max_length=100,default="")
    image1 = models.ImageField(upload_to="myShop/images", default="")
    image2 = models.ImageField(upload_to="myShop/images", default="")
    image3 = models.ImageField(upload_to="myShop/images", default="")
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    def __str__(self):
        return self.name

class Electronicstationary(models.Model):
    products_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256,default="")
    short_description = models.CharField(max_length=100, default="")
    description = models.CharField(max_length=256,default="")
    category = models.CharField(max_length=100,default="")
    image1 = models.ImageField(upload_to="myShop/images", default="")
    image2 = models.ImageField(upload_to="myShop/images", default="")
    image3 = models.ImageField(upload_to="myShop/images", default="")
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    def __str__(self):
        return self.name

class Printing_material(models.Model):
    products_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256,default="")
    short_description = models.CharField(max_length=100, default="")
    description = models.CharField(max_length=256,default="")
    category = models.CharField(max_length=100,default="")
    image1 = models.ImageField(upload_to="myShop/images", default="")
    image2 = models.ImageField(upload_to="myShop/images", default="")
    image3 = models.ImageField(upload_to="myShop/images", default="")
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    def __str__(self):
        return self.name


