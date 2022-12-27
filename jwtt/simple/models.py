from django.db import models

# Create your models here.
class Employee(models.Model):
    name=models.CharField(max_length=50)
    slug=models.SlugField(max_length=50, null=True, unique=True)
    address=models.CharField(max_length=100)
    phone= models.IntegerField()
    email=models.EmailField(max_length=100)
    age=models.IntegerField()
    
    def __str__(self):
        return self.name

        
class Salary(models.Model):
    salary=models.IntegerField()
    salary_get=models.BooleanField()
    employee=models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='salary')
