from django.shortcuts import render
from .models import Product, Category
from rest_framework import viewsets
from .serializers import ProductSerializer, CategorySerializer

# Create your views here.
class ProductViewset(viewsets.ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer

class CategoryViewset(viewsets.ModelViewSet):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer