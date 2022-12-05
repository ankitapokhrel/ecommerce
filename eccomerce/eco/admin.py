from django.contrib import admin
from .models import Customer, User, Item

# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display= ['id', 'u_name', 'contact', 'email']

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display =  ['id', 'c_name', 'address', 'contact', 'email']

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display=['id', 'item', 'item_type', 'price']