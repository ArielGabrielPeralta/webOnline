from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User
# Create your views here.


def home(request):
    return render(request, 'webApp/home.html')
