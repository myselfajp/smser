from .views import *
from django.urls import path

app_name="panel"

urlpatterns = [

    path("",http_panel_home,name='blog-home'),
    
    
]
