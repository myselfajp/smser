from azbankgateways.urls import az_bank_gateways_urls
from django.conf.urls.static import static
from django.urls import path , include
from django.conf import settings
from django.contrib import admin
# admin.autodiscover()


urlpatterns = [

    path('bankgateways/', az_bank_gateways_urls()),

    path('payment/',include('payment.urls')),

    path('panel/',include('panel.urls')),

    path('girisadmin/', admin.site.urls),

    path('',include('users.urls')),

]
urlpatterns += static(settings.STATIC_URL)