from rest_framework import serializers

from .models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('balance', 'name', 'surname')
        read_only_fields = ('is_active', )
