from django.contrib import admin
from .models import Product, Variation,Category,ProductImage
# Register your models here.
admin.site.register(Product)
admin.site.register(Variation)
admin.site.register(Category)
admin.site.register(ProductImage)
