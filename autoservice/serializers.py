from rest_framework import serializers

from autoservice.models import Autoservice, Car


class AutoserviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autoservice
        fields = ('is_active', 'id', 'name', 'feature_preference', 'balance')
        read_only_fields = ('is_active', )


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'
        read_only_fields = ('is_active', )
