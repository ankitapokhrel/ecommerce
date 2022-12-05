from django.shortcuts import render
from .models import Customer, User, Item
from .serializers import CustomerSerializer, UserSerializer, ItemSerializer
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class CustomerViewSet(viewsets.ModelViewSet):
    queryset= Customer.objects.all()
    serializer_class=CustomerSerializer
    authentication_classes=[SessionAuthentication]

class UserViewSet(viewsets.ModelViewSet):
    queryset= User.objects.all()
    serializer_class=UserSerializer
    authentication_classes=[SessionAuthentication]
    permission_classes=[IsAuthenticated]

class ItemViewSet(viewsets.ModelViewSet):
    queryset= Item.objects.all()
    serializer_class=ItemSerializer
    

