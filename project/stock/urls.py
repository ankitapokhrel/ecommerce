from django.urls import path, include
from stock import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('Stock', views.StockViewset)


urlpatterns = [
    path('', include(router.urls)),
]
