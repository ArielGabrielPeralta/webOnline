from django.shortcuts import render, HttpResponse

# Create your views here.


def home(request):
    return HttpResponse('Home')


def service(request):
    return HttpResponse('Service')


def shop(request):
    return HttpResponse('Shop')


def blog(request):
    return HttpResponse('Blog')


def contact(request):
    return HttpResponse('Contact')
