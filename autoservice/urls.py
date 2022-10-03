from rest_framework import routers

from .views import AutoserviceViewSet, CarViewSet

urlpatterns = [
    ########
]
router = routers.SimpleRouter()
router.register(r'autoservice', AutoserviceViewSet)
router.register(r'car', CarViewSet)

urlpatterns += router.urls
