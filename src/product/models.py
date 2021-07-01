from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField
from django.utils.safestring import mark_safe

# Create your models here.
class ProductImage(models.Model):
    alt = models.TextField()
    file = ThumbnailerImageField(upload_to="products")
    variation = models.ForeignKey("Variation",on_delete=models.CASCADE,related_name="image")
    def __str__(self):
        return self.alt


    def image(self):
        return mark_safe('<a href="{0}" target="_blank">'
                        '<img src="{1}" width="150" height="150" />'
                        '</a>'.format(self.file.url, self.file['admin_preview'].url)
                         )
    def image_icon(self):
        return mark_safe('<a href="{0}" target="_blank">'
                        '<img src="{1}" width="100" height="100" />'
                        '</a>'.format(self.file.url, self.file['admin_preview_icon'].url)
                         )



class Category(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)
    created_At = models.DateTimeField(auto_now_add=True)
    updated_At = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Variation(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name="variations")
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=11,decimal_places=2)
    sale_price = models.DecimalField(max_digits=11,decimal_places=2)
    description = models.TextField()
    created_At = models.DateTimeField(auto_now_add=True)
    updated_At = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name