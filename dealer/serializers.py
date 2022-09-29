from rest_framework import serializers

from .models import Dealer


class DealerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dealer
        fields = ('name', 'year_of_creation')
        read_only_fields = ('is_active', )