from django.shortcuts import render

from .models import Product
from .models import Category


# Create your views here.
def product_list(request):
    categories = Category.objects.filter(product__isnull=False).distinct()
    category = request.GET.get("category",0)
    search = request.GET.get("search")
    if category:
        products = Product.objects.filter(category=category)
    else:
        products = Product.objects.all()
    if search:
        products = products.filter(name__contains=search)
    return render(request,"product/list.html",{"category_id":int(category),"products":products,"categories":categories}) 

def product_detail(request,id):
    product = Product.objects.get(id=id)
    variation = request.GET.get("variation")
    if variation:
        variation = product.variations.get(id=variation)
    else:
        variation = product.variations.first()
    
    return render(request,"product/detail.html",{"product":product,"variation":variation})