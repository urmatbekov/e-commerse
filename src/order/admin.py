from django.contrib import admin
from django.db import models

from user.models import BillingAddress, ShippingAddress
from .models import Cart, CartItem, Order
# Register your models here.

# CART


class InlineCartItem(admin.TabularInline):
    model = CartItem
    extra = 0
    readonly_fields = ["product", "quantity", "price", "line_price"]


@admin.register(Cart)
class AdminCart(admin.ModelAdmin):
    list_display = ["total_price", "active", "created_At", "updated_At"]
    inlines = [InlineCartItem]
    readonly_fields = ["total_price"]


### CART ITEM

@admin.register(CartItem)
class AdminCartItem(admin.ModelAdmin):
    list_display = ["product", "quantity", "price", "line_price", "cart"]
    readonly_fields = ["product", "quantity", "price", "line_price", "cart"]

### ORDER

@admin.register(Order)
class AdminOrder(admin.ModelAdmin):
    list_display = ["user", "shipping_address",
                    "billing_address", "status", "created_At", "updated_At"]
    list_filter = ["status", "user"]
   

