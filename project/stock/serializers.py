from rest_framework import serializers
from .models import Stock
from product.models import Product

class StockSerializer(serializers.ModelSerializer):
    product_name=serializers.ReadOnlyField(source='product.name')
    product_min_qty=serializers.ReadOnlyField(source='product.minimum_stock_qty')
    product_max_qty=serializers.ReadOnlyField(source='product.maximum_stock_qty')
    class Meta:
        model=Stock
        fields='__all__'


    def validate(self, attrs):
        qty=attrs.get('qty')
        product=attrs.get('product')
        min_product_qty=product.minimum_stock_qty
        max_product_qty=product.maximum_stock_qty
               
        if min_product_qty>qty:
            raise serializers.ValidationError({'msg': "entered quantity is less than the product minimum quantity"})

        elif max_product_qty<qty:
            raise serializers.ValidationError({'msg': "entered quantity is more than the product maximum quantity"}) 

        return attrs