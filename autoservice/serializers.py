from rest_framework import serializers

from autoservice.models import Autoservice, Car


class AutoserviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autoservice
        fields = '__all__'
        read_only_fields = ('is_active', 'balance',)


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'
        read_only_fields = ('is_active', )
