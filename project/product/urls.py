from product import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('Product', views.ProductViewset, basename='product')
router.register('Category', views.CategoryViewset, basename='category')

urlpatterns = [
    path('', include(router.urls)),
    
]