from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, ShippingAddress, BillingAddress, District
# Register your models here.

### USER
class InlineShippingAdress(admin.TabularInline):
    model = ShippingAddress
    extra = 0
    show_change_link = True


class InlineBiullingAdress(admin.TabularInline):
    model = BillingAddress
    extra = 0
    show_change_link = True



UserAdmin.inlines = [InlineShippingAdress,InlineBiullingAdress]

admin.site.register(User,UserAdmin)
admin.site.register(ShippingAddress)
admin.site.register(BillingAddress)
admin.site.register(District)
