from django.contrib import admin
from .models import Slider
# Register your models here.
@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ["image_icon","title","description","active"]
    fields = ["image_tag","image","title","description","active"]
    readonly_fields = ["image_tag","image_icon"]
    list_display_links = ["title"]