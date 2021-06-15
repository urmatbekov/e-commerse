from django.contrib import admin
from .models import Product, Variation,Category,ProductImage
# Register your models here.

class InlineVariation(admin.StackedInline):
    model = Variation
    min_num = 1
    extra = 0
    show_change_link = True


class AdminProduct(admin.ModelAdmin):
    list_display = ["name","description"]
    inlines = [InlineVariation]

admin.site.register(Product,AdminProduct)



class InlineProductImage(admin.TabularInline):
    model = ProductImage
    min_num = 1
    extra = 0


class AdminVariation(admin.ModelAdmin):
    list_display = ["name","description"]
    inlines = [InlineProductImage]

admin.site.register(Variation,AdminVariation)









class AdminCategory(admin.ModelAdmin):
    list_display = ["name","description"]

admin.site.register(Category,AdminCategory)

class AdminProductImage(admin.ModelAdmin):
    list_display = ["file","alt"]
admin.site.register(ProductImage,AdminProductImage)
