from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, ShippingAddress, BillingAddress, District
# Register your models here.

admin.site.register(User,UserAdmin)
admin.site.register(ShippingAddress)
admin.site.register(BillingAddress)
admin.site.register(District)
