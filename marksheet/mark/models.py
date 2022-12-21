from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 

# Create your models here.
class Student(models.Model):
    s_name = models.CharField(max_length=100)
    roll= models.IntegerField(unique=True)
    address=models.CharField(max_length=50)

    def __str__(self):
        return  '{}'.format(self.s_name)    # returning student name from class.

class Marks(models.Model):
    subject=models.CharField(max_length=100)
    marks=models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    student=models.ForeignKey(Student, on_delete=models.CASCADE, related_name='marks')






