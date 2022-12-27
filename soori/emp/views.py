from django.shortcuts import render
from .models import Employee, Salary
from .serializers import EmployeeSerializer, SalarySerializer
from rest_framework import viewsets

# Create your views here.
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer

class SalaryeViewSet(viewsets.ModelViewSet):
    queryset=Salary.objects.all()
    serializer_class=SalarySerializer