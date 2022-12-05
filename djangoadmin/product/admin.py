from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Product

@admin.register(Product)

# ModelAdmin Class # DataFlair
class ProductAdmin(admin.ModelAdmin):
    # exclude=('description')
    list_display = ['name', 'description', 'mfg_date']
    list_filter = ['mfg_date', ]

# Register your models here.
# DataFlair

# admin.site.unregister(Group)

# ##changing the admin header
# admin.site.site_header = "DataFlair Django Tutorials"