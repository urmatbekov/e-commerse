from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField

# Create your models here.
class ProductImage(models.Model):
    alt = models.TextField()
    file = ThumbnailerImageField(upload_to="products")
    variation = models.ForeignKey("Variation",on_delete=models.CASCADE,related_name="image")

class Category(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ManyToManyField(Category)
    created_At = models.DateTimeField(auto_now_add=True)
    updated_At = models.DateTimeField(auto_now=True)

class Variation(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name="variations")
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=11,decimal_places=2)
    sale_price = models.DecimalField(max_digits=11,decimal_places=2)
    description = models.TextField()
    created_At = models.DateTimeField(auto_now_add=True)
    updated_At = models.DateTimeField(auto_now=True)