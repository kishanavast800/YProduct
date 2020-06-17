from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=100,default="")
    pub_date = models.DateField()
    image = models.ImageField(upload_to="myShop/images", default="")
    def __str__(self):
        return self.product_name
