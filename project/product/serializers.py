from rest_framework import serializers
from .models import Product, Category

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=['id','name', 'manufacture_name', 'minimum_stock_qty', 'maximum_stock_qty', 'expiry_date', 'category', 'sub_category']

class CategorySerializer(serializers.ModelSerializer):
    product=ProductSerializer(read_only=True, many=True)
    class Meta:
        model=Category
        fields=['category', 'sub_category', 'product']