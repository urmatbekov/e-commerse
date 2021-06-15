from django.contrib import admin
from .models import Product, Variation,Category,ProductImage
# Register your models here.

### PRODUCT
class InlineVariation(admin.StackedInline):
    model = Variation
    min_num = 1
    extra = 0
    show_change_link =True


@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display = ["name","description","get_category"]
    inlines = [InlineVariation]

### VARITION
class InlineProductImage(admin.TabularInline):
    model = ProductImage
    min_num = 1
    extra = 0

@admin.register(Variation)
class AdminVariation(admin.ModelAdmin):
    list_display = ["name","description","price","sale_price","created_At","updated_At"]
    inlines = [InlineProductImage]


### CATEGORY
class InlineProduct(admin.TabularInline):
    model = Product.category.through
    extra = 0

@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ["name","description"]
    inlines = [InlineProduct]

### IMAGE
@admin.register(ProductImage)
class AdminProductImage(admin.ModelAdmin):
    list_display = ["file","alt"]

