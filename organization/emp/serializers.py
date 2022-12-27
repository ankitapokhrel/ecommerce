from .models import Employee, Salary
from rest_framework import serializers

class SalarySerializer(serializers.ModelSerializer):
    class Meta:
        model=Salary 
        fields= '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    salary=SalarySerializer(many=True, read_only=True)
    class Meta:
        model=Employee
        fields='__all__'