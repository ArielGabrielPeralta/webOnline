from django.urls import path

from webApp import views
from . import views
urlpatterns = [
    path('', views.contact, name='Contact'),
]
