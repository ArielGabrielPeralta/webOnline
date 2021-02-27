from django.urls import path
from webApp import views

urlpatterns = [
    path('', views.home, name='Home'),
    path('service', views.service, name='Service'),
    path('shop', views.shop, name='Shop'),
    path('blog', views.blog, name='Blog'),
    path('contact', views.contact, name='Contact'),
]
