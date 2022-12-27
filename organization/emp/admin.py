from django.contrib import admin
from .models import Employee, Salary

# Register your models here.
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    # list_display=['id', 'name', 'address', 'phone', 'email']
    {
        'fields': (('name', 'address'), 'address', 'city', 'state'),
    }
    

@admin.register(Salary)
class SalaryAdmin(admin.ModelAdmin):
    list_display=['id', 'salary', 'salary_get']