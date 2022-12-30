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

    # def post(self, request, format=None):
    #     serializer=StockSerializer
    #     qty=serializer.data.get('qty')
    #     product_qty=request.data
    #     print(product_qty)

        # if qty<product_qty:
        #     return Response({'msg': 'Sorry, the product quantity you entered is not available'})
                
        # else:
        #     return Response("You can proceed your operation")

