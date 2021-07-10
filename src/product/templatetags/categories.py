from django import template
from product.models import Category
register = template.Library()

@register.simple_tag
def get_categories():
    return Category.objects.filter(product__isnull=False).distinct()