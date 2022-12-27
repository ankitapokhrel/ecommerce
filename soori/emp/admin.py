from django.contrib import admin
from .models import Salary, Employee

# Register your models here.
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display= ['id', 'name', 'gender', 'age', 'phone', 'address', 'email_id']

@admin.register(Salary)
class SalaryAdmin(admin.ModelAdmin):
    list_display=['id', 'salary', 'salary_dist']