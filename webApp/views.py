from django.shortcuts import render, HttpResponse

# Create your views here.


def home(request):
    return render(request, 'webApp/home.html')


def shop(request):
    return render(request, 'webApp/shop.html')
