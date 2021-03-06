from django.shortcuts import render
from shopApp.models import Product, ProductCategory

# Create your views here.


def shop(request):
    product_list = Product.objects.all()
    categories = ProductCategory.objects.all()
    return render(request, 'shopApp/shop.html', {"products": product_list, "categories": categories})


def productcategory(request, category_id):
    category = ProductCategory.objects.get(id=category_id)
    product = Product.objects.filter(product_categories=category)
    return render(request, 'shopApp/categories.html', {'categories': category, 'products': product})
