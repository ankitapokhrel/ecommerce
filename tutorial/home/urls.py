from django.contrib import admin
from django.urls import path
from home import views
from .views import *

urlpatterns = [
    path("", home, name='home'),
    path('post_todo/', post_todo, name="post_todo")
    # path("about", views.about, name='about'),
    # path("services", views.services, name='services'),
    # path("contact", views.contact, name='contact'),
    
]