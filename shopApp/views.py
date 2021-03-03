from django.shortcuts import render
from .models import Product

# Create your views here.


def shop(request):
    product_list = Product.objects.all()
    return render(request, 'shopApp/shop.html', {"products": product_list})
