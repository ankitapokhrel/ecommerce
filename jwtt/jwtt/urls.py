from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.routers import DefaultRouter
from simple import views

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router=DefaultRouter()

router.register('Employee', views.EmployeeViewSet, basename='employee')
router.register('Salary', views.SalaryViewSet, basename='salary')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path ('auth/', include('rest_framework.urls', 'rest_framework')), 
    path('gettoken/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refreshtoken/', TokenRefreshView.as_view(), name='token_refresh'),
]
