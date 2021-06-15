from django.contrib import admin
from .models import Cart,CartItem,Order
# Register your models here.

### CART

class InlineCartItem(admin.TabularInline):
    model = CartItem
    extra = 0
    readonly_fields = ["product","quantity","price","line_price"]

@admin.register(Cart)
class AdminCart(admin.ModelAdmin):
    list_display = ["total_price","active","created_At","updated_At"]
    inlines = [InlineCartItem]
    readonly_fields = ["total_price"]
    


admin.site.register(CartItem)
admin.site.register(Order)