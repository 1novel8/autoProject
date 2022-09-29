from rest_framework import viewsets
from rest_framework import mixins

from .models import Autoservice, Car
from .serializers import AutoserviceSerializer, CarSerializer


class AutoserviceViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                         mixins.CreateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = Autoservice.objects.filter(is_active=True)
    serializer_class = AutoserviceSerializer

    def perform_destroy(self, instance: Autoservice):
        instance.is_active = False
        instance.save()


class CarViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                 mixins.CreateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = Car.objects.filter(is_active=True)
    serializer_class = CarSerializer

    def perform_destroy(self, instance: Autoservice):
        instance.is_active = False
        instance.save()
