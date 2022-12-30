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

    # def create(self, validated_data):
    #     # print('Hello')
    #     # print(validated_data)
    #     qty=validated_data['qty']
    #     product_qty=validated_data['product'].minimum_stock_qty
    #     print(product_qty, 'asdhagdghahg')
    #     stock =Stock.objects.create(**validated_data)
    #     print(stock.product.minimum_stock_qty,'message')
    #     if product_qty<qty:
    #         serializers.ValidationError({'msg': "quantity is less"})
           
    #     return stock
            

    # def validate(self, attrs):
    #     password=attrs.get('password')
    #     password2=attrs.get('password2')
    #     user=self.context.get('user')
    #     if password!=password2:
    #         raise serializers.ValidationError("password and confirm password doesn't match") 
    #     user.set_password(password)
    #     user.save()
    #     return attrs

    def validate(self, attrs):
        qty=attrs.get('qty')
        product=attrs.get('product')
        min_product_qty=product.minimum_stock_qty
        max_product_qty=product.maximum_stock_qty
               
        if min_product_qty>qty:
         
            raise serializers.ValidationError({'msg': "stock quantity is less than minimum product stock quantity"})

        elif max_product_qty<qty:
            raise serializers.ValidationError({'msg': "entered quantity is more than the product maximum quantity"}) 

        return attrs