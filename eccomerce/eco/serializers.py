from rest_framework import serializers
from .models import Customer, User, Item
from django.db.models import Max

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model= Item
        fields = ['id', 'item', 'item_type', 'price']

class CustomerSerializer(serializers.ModelSerializer):
    total_amount=serializers.SerializerMethodField()
    highest_price= serializers.SerializerMethodField()
    items=ItemSerializer(many=True, read_only=True)
    class Meta:
        model= Customer
        fields = ['id', 'c_name', 'address', 'contact', 'email', 'total_amount', 'highest_price', 'items']

    def get_total_amount(self, customer):
        total_amount= sum(Item.objects.filter(customer=customer).values_list('price', flat=True))
        return total_amount    

    def get_highest_price(self, customer):
        highest_price =Item.objects.filter(customer=customer).values('price').aggregate(Max('price'))  
        return highest_price

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields = ['id', 'u_name', 'contact', 'email']


