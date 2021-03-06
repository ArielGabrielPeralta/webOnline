from django.urls import path

from . import views

urlpatterns = [
    path('', views.shop, name='Shop'),
    path('category/<int:category_id>/',
         views.productcategory, name='ProductCategory'),

]
