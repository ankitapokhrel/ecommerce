from django.contrib import admin
from .models import Product, Category

# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=['id', 'name', 'manufacture_name', 'minimum_stock_qty', 'expiry_date', 'category', 'sub_category']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=['id', 'category', 'sub_category', 'product', 'prod']