from django.db import models

# Create your models here.
class Customer(models.Model):
    c_name= models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    contact=models.IntegerField()
    email=models.EmailField(max_length=100)

    def __str__(self):
        return '{}'.format(self.c_name)

class User(models.Model):
    u_name= models.CharField(max_length=50)
    contact=models.IntegerField()
    email=models.EmailField(max_length=100)

class Item(models.Model):
    item= models.CharField(max_length=100)
    item_type=models.CharField(max_length=100)
    price=models.IntegerField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='items')
