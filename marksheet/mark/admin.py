from django.contrib import admin
from .models import Student, Marks
# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=['id', 'roll', 's_name', 'address']


@admin.register(Marks)
class MarksAdmin(admin.ModelAdmin):
    list_display=['id', 'marks', 'subject', 'student']

