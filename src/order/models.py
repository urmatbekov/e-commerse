from django.db import models
from django.db.models.base import Model
from product.models import Product
from django.contrib.auth import get_user_model

from user.models import BillingAddress, ShippingAddress

User = get_user_model()

# Create your models here.
class Cart(models.Model):
    total_price = models.DecimalField(max_digits=11,decimal_places=2)
    active = models.BooleanField(default=True)

class CartItem(models.Model):
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)
    quantity = models.SmallIntegerField()
    price = models.DecimalField(max_digits=11,decimal_places=2)
    line_price = models.DecimalField(max_digits=11,decimal_places=2)
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE)


ORDER_STATUS = [
    ('created',"Created"),
    ('completed',"Completed"),
    ('refused',"Refused")
]


class Order(models.Model):
    cart = models.OneToOneField(Cart,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    shipping_address = models.ForeignKey(ShippingAddress,on_delete=models.SET_NULL,null=True)
    billing_address = models.ForeignKey(BillingAddress,on_delete=models.SET_NULL,null=True)
    status = models.CharField(max_length=10,choices=ORDER_STATUS)
    


