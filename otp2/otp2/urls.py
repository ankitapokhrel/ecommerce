from django.contrib import admin
from django.urls import path
from account.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sendotp/', send_otp), 
    # path('')
]