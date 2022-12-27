from django.db import models

# Create your models here.
GENDER_CHOICES=('Male', "M"), ('Female', "F"),

class Employee(models.Model):
    name=models.CharField(max_length=20)
    gender=models.CharField(max_length=10, choices=GENDER_CHOICES, default='1')
    age=models.IntegerField()
    phone=models.IntegerField()
    address=models.CharField(max_length=50)
    email_id=models.EmailField(max_length=50)

    def __str__(self):
        return '{}'.format(self.name)

class Salary(models.Model):
    salary=models.IntegerField()
    salary_dist=models.BooleanField()
    employee=models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='salary')
