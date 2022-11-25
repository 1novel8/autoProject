from rest_framework import mixins, viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from autoservice.serializers import CarSerializer
from .models import Dealer, DealerCarCatalog, DealerSaleHistory
from .serializers import DealerSerializer
from .tasks import send_spam
from .services import DealerService


class DealerViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = Dealer.objects.filter(is_active=True)
    serializer_class = DealerSerializer
    car_serializer = CarSerializer
    dealer_service = DealerService()

    def perform_destroy(self, instance: Dealer):
        instance.is_active = False
        instance.save()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        # send_spam.delay(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @action(methods=['GET'], detail=True)
    def get_car_catalog(self, request, pk):
        query_set = DealerCarCatalog.objects.select_related('car').filter(dealer_id=pk)
        return Response(self.dealer_service.get_car_catalog(query_set), status=status.HTTP_200_OK)

    @action(methods=['GET'], detail=True)
    def get_sale_history(self, request, pk):
        query_set = DealerSaleHistory.objects.select_related('car').filter(dealer_id=pk)
        return Response(self.dealer_service.get_sale_history(query_set), status=status.HTTP_200_OK)
