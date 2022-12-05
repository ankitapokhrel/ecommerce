from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from .models import Student, Marks
from .serializers import StudentSerializer, MarksSerializer
from rest_framework import status
# from rest_framework.decorators import action

# Create your views here.

class StudentViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

class MarksViewSet(viewsets.ModelViewSet):
    queryset=Marks.objects.all()
    serializer_class=MarksSerializer

