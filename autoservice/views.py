from rest_framework import viewsets, status
from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Autoservice, Car, AutoserviceSaleHistory, AutoserviceCarCatalog
from .serializers import AutoserviceSerializer, CarSerializer
from .services import AutoserviceService


class AutoserviceViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                         mixins.CreateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = Autoservice.objects.filter(is_active=True)
    serializer_class = AutoserviceSerializer
    autoservice_service = AutoserviceService()

    def perform_destroy(self, instance: Autoservice):
        instance.is_active = False
        instance.save()

    @action(methods=['GET'], detail=True)
    def get_car_catalog(self, request, pk):
        query_set = AutoserviceCarCatalog.objects.select_related('car').filter(autoservice_id=pk)
        return Response(self.autoservice_service.get_car_catalog(query_set), status=status.HTTP_200_OK)

    @action(methods=['GET'], detail=True)
    def get_sale_history(self, request, pk):
        query_set = AutoserviceSaleHistory.objects.select_related('car').filter(autoservice_id=pk)
        return Response(self.autoservice_service.get_sale_history(query_set), status=status.HTTP_200_OK)


class CarViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                 mixins.CreateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = Car.objects.filter(is_active=True)
    serializer_class = CarSerializer

    def perform_destroy(self, instance: Autoservice):
        instance.is_active = False
        instance.save()
