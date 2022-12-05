
### use of concrete view class(we need queryset and serializer_class codes under the created class.

from django.shortcuts import render
from .models import Student
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import StudentSerializer
# Create your views here.
class StudentListCreate(ListCreateAPIView):
    queryset= Student.objects.all()
    serializer_class = StudentSerializer

class StudentRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset=Student.objects.all()
    serializer_class = StudentSerializer
