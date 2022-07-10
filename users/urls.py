from .views import *
from django.urls import path

# app_name="users"

urlpatterns = [

    path("",http_panel_home,name='blog-home'),
    path("login/",http_login,name='login'),
    path("verify/",http_verify,name='verify'),
    path("profile/",http_profile,name='profile'),

    
]
