from rest_framework import serializers

from .models import Dealer


class DealerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dealer
        fields = '__all__'
        read_only_fields = ('id', 'date_of_creation', 'date_of_last_modification',  'is_active',
                            'count_of_buyers', 'car_catalog', )
