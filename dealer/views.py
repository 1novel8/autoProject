from rest_framework import mixins, viewsets, status
from rest_framework.response import Response

from .models import Dealer
from .serializers import DealerSerializer
from .tasks import send_spam


class DealerViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = Dealer.objects.filter(is_active=True)
    serializer_class = DealerSerializer

    def perform_destroy(self, instance: Dealer):
        instance.is_active = False
        instance.save()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        send_spam.delay(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

