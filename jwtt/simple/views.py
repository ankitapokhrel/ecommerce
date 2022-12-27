from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Employee, Salary
from .serializers import SalarySerializer, EmployeeSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    # authentication_class=[JWTAuthentication]
    # permission_classes=[IsAuthenticated]
    
    
class SalaryViewSet(viewsets.ModelViewSet):
    queryset= Salary.objects.all()
    serializer_class=SalarySerializer

    @action(detail=False, methods='POST')  # this code is not working
    def get_dsc_salary(self, request, **kwargs):
        data={}
        dsc_salary=request.Salary.objects.all().order_by('-salary').values()
        data['dsc']= dsc_salary
        return Response(data, status=status.HTTP_200_OK)


