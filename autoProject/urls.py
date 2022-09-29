from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('autoservice/', include('autoservice.urls')),
    path('customer/', include('customer.urls')),
    path('dealer/', include('dealer.urls')),
]
