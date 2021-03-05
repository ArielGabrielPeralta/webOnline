from django.shortcuts import render
from shopApp.models import Product, ProductCategory

# Create your views here.


def shop(request):
    product_list = Product.objects.all()
    categories = ProductCategory.objects.all()
    return render(request, 'shopApp/shop.html', {"products": product_list, "categories": categories})


def productcategory(request, product_categories_id):
    category = ProductCategory.objects.get(id=product_categories_id)
    products = Product.objects.filter(categories=category)
    return render(request, 'shopApp/categories.html', {'category': category, 'product': products})
