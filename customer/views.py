from rest_framework import mixins
from rest_framework import viewsets

from .models import Customer
from .serializers import CustomerSerializer


class CustomerViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = Customer.objects.filter(is_active=True)
    serializer_class = CustomerSerializer

    def perform_destroy(self, instance: Customer):
        instance.is_active = False
        instance.save()
