from django.db import models
from product.models import Product

class Stock(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    qty=models.IntegerField()

    

