from rest_framework import serializers
from .models import Customer, User, Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model= Item
        fields = ['id', 'item', 'item_type', 'price']

        

class CustomerSerializer(serializers.ModelSerializer):
    total_amount=serializers.SerializerMethodField()
    items=ItemSerializer(many=True, read_only=True)
    class Meta:
        model= Customer
        fields = ['id', 'c_name', 'address', 'contact', 'email', 'total_amount', 'items']

    def get_total_amount(self, customer):
        total_amount= sum(Item.objects.filter(customer=customer).values_list('price', flat=True))
        return total_amount    
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields = ['id', 'u_name', 'contact', 'email']


