from django.shortcuts import render
from rest_framework import viewsets
from product.models import *
from rest_framework.response import Response
from .serializers import StockSerializer
from .models import Stock


# Create your views here.
class StockViewset(viewsets.ModelViewSet):
    queryset=Stock.objects.all()
    serializer_class=StockSerializer

   