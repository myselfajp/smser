from django.urls import path
from payment.views import go_to_gateway_view,callback_gateway_view

# app_name="users"

urlpatterns = [
    path("",go_to_gateway_view,name='payment'),
    path("callback_payment/",callback_gateway_view,name='callback'),
    
]






