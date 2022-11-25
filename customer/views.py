from requests import Response
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from authorization.models import User
from .models import Customer
from .serializers import CustomerSerializer


class CustomerViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = Customer.objects.filter(is_active=True)
    serializer_class = CustomerSerializer
    permission_classes = (IsAuthenticated, )

    def perform_destroy(self, instance: Customer):
        instance.is_active = False
        instance.save()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        if instance.user == request.user:
            return Response(serializer.data)
