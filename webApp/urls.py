from django.urls import path
from webApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='Home'),
    path('service', views.service, name='Service'),
    path('shop', views.shop, name='Shop'),
    path('blog', views.blog, name='Blog'),
    path('contact', views.contact, name='Contact'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
