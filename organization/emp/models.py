from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify 


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

        
    def get_absolute_url(self):
        return reverse("employee-detail", kwargs={'slug':self.slug})

    def save(self, *args, **kwargs):  
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

class Salary(models.Model):
    salary=models.IntegerField()
    salary_get=models.BooleanField()
    employee=models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='salary')


