from django.contrib import admin
from .models import Product, Variation,Category,ProductImage
from jet.admin import CompactInline
# Register your models here.

### PRODUCT
class InlineVariation(CompactInline):
    model = Variation
    min_num = 1
    extra = 0
    show_change_link =True


@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display = ["name","description"]
    inlines = [InlineVariation]

### VARITION
class InlineProductImage(CompactInline):
    model = ProductImage
    fields = ["image","file","alt"]
    min_num = 1
    extra = 0
    readonly_fields = ["image"]

@admin.register(Variation)
class AdminVariation(admin.ModelAdmin):
    list_display = ["name","description","price","sale_price","created_At","updated_At"]
    inlines = [InlineProductImage]


### CATEGORY
class InlineProduct(CompactInline):
    model = Product
    extra = 0
    show_change_link = True

@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ["image_icon","name","description"]
    fields = ["image_tag","image","name","description"]
    readonly_fields = ["image_tag","image_icon"]
    inlines = [InlineProduct]

### IMAGE
@admin.register(ProductImage)
class AdminProductImage(admin.ModelAdmin):
    fields = ["image_icon","alt","variation"]
    list_display = ["id","image_icon","file","alt"]
    readonly_fields = ["image_icon"]

