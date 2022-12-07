"""eccomerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from eco import views
from rest_framework_swagger.views import get_swagger_view
# from django.conf.urls import url

# schema_view = get_swagger_view(title='Pastebin API')

# urlpatterns = [
#     url(r'^$', schema_view)
# ]



from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView


router=DefaultRouter()

router.register('Customer', views.CustomerViewSet, basename='customer')
router.register('User', views.UserViewSet, basename='user')
router.register('Item', views.ItemViewSet, basename='item')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', 'rest_framework')),

    # for the application of swagger-ui. 
    path('api/doc', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),

]
