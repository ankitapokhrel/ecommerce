
from django.urls import path 
from core import views
from . import views
urlpatterns = [
        path('learndj/', views.learn_django),
]
