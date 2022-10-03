from rest_framework import mixins, viewsets

from .models import Dealer
from .serializers import DealerSerializer


class DealerViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = Dealer.objects.filter(is_active=True)
    serializer_class = DealerSerializer

    def perform_destroy(self, instance: Dealer):
        instance.is_active = False
        instance.save()

    # @action()
    # def listOf(self, request):
    #     dew
