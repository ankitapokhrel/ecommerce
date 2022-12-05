
### use of model viewset in drf (combines the code and reduces the logic of codes, using router in urls.py, the code complexity reduces.)
from .models import Student
from rest_framework import viewsets
from .serializers import StudentSerializer
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.
class StudentModelViewSet(viewsets.ModelViewSet): 
    queryset= Student.objects.all()
    serializer_class=StudentSerializer
    authentication_classes= [SessionAuthentication]
    permission_classes=[IsAuthenticated]

