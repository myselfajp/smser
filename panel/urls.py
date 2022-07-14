from django.urls import path
from .views import  send_sms
# app_name="users"

urlpatterns = [
    path("",send_sms,name='panel'),
    
]

