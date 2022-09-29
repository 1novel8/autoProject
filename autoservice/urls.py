from rest_framework import routers

from .views import AutoserviceViewSet, CarViewSet

urlpatterns = [
    ########
]
router = routers.SimpleRouter()
router.register(r'', AutoserviceViewSet)
router.register(r'', CarViewSet)

urlpatterns += router.urls

