from django.db import models

# Create your models here.


class ProductCategory(models.Model):
    name = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'product category'
        verbose_name_plural = 'product categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50)
    descrption = models.CharField(max_length=50)
    price = models.FloatField()
    image = models.ImageField(upload_to='shop', null=True, blank=True)
    brand = models.CharField(max_length=50)
    available = models.BooleanField(default=True)
    product_categories = models.ForeignKey(
        ProductCategory, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def __str__(self):
        return self.name
