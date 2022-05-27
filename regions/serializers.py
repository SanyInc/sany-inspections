from rest_framework import serializers
from .models import ZipCode, State, Region, RegionUnity

class ZipCodeSerializer(serializers.ModelSerializer):
    number = serializers.IntegerField()
    
    class Meta:
        model = ZipCode
        fields = ['id', 'number']

class StateSerializer(serializers.ModelSerializer):
    zip_codes = ZipCodeSerializer(many=True, read_only=True)

    class Meta:
        model = State
        fields = ['id', 'title', 'zip_codes']

class RegionUnitySerializer(serializers.ModelSerializer):
    states = StateSerializer(many=True, read_only=True)

    class Meta:
        model = RegionUnity
        fields = ['id', 'title', 'states']

class RegionSerializer(serializers.ModelSerializer):
    region_unities = RegionUnitySerializer(many=True, read_only=True)

    class Meta:
        model = Region
        fields = ['id', 'title', 'region_unities']












