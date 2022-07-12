from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
from azbankgateways.urls import az_bank_gateways_urls
# admin.autodiscover()


urlpatterns = [
    path('bankgateways/', az_bank_gateways_urls()),
    path('payment/',include('payment.urls')),
    path('admin/', admin.site.urls),
    path('',include('users.urls')),
        

]
urlpatterns += static(settings.STATIC_URL)