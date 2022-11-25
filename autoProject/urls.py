from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('autoservice.urls')),
    path('customer/', include('customer.urls')),
    path('', include('dealer.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('auth/', include('djoser.urls')),
    path('user/', include('authorization.urls')),
    path('auth/', include('djoser.urls.jwt')),

]
