from django.db import models

# Create your models here.
class Category(models.Model):
    category=models.IntegerField()
    sub_category=models.CharField(max_length=30)

    def __str__(self):
        return "'{}','{}'".format(self.category, self.sub_category)
            
class Product(models.Model):
    name=models.TextField(unique=True)
    manufacture_name=models.TextField()
    minimum_stock_qty=models.IntegerField()
    maximum_stock_qty=models.IntegerField()
    expiry_date=models.DateField()
    category=models.ForeignKey(Category, on_delete=models.CASCADE, related_name='product')
    sub_category=models.ForeignKey(Category, on_delete=models.CASCADE, related_name='prod')

    def __str__(self):
        return '{}'.format(self.name)
    
