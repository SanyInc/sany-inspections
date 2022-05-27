from rest_framework import serializers
from .models import Store, Business
from accounts.serializers import BusinessOwnerListSerializer, HealthRegulatorListSerializer
from checklists.serializers import ActivityDetailSerializer

class BusinessCreateSerializer(serializers.ModelSerializer):  
    class Meta:
        model = Business
        fields = '__all__'

class BusinessListSerializer(serializers.ModelSerializer):
    owner=BusinessOwnerListSerializer()

    class Meta:
        model = Business
        fields = '__all__'

class BusinessDetailSerializer(serializers.ModelSerializer):
    owner=BusinessOwnerListSerializer()
    stores = 'StoreListSerializer(many=True, read_only=True)'

    class Meta:
        model = Business
        fields = ['id', 'title', 'slug', 'owner',
                   'vat', 'stores']
        extra_kwargs = {'url': {'lookup_field': 'slug'}}

class StoreCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = '__all__'

class StoreListSerializer(serializers.ModelSerializer):

    region_unity = serializers.StringRelatedField()
    region = serializers.StringRelatedField()
    state = serializers.StringRelatedField()
    zip_code = serializers.StringRelatedField()
    business = serializers.StringRelatedField()
    activity = serializers.StringRelatedField()
    type_of_activity = serializers.StringRelatedField()
    # healthregulator = serializers.StringRelatedField()
    # inspections= InspectionSerializer(many=True, read_only=True)

    class Meta:
        model = Store
        fields = [
            'id',
            'business',
            'category',
            'slug',
            # 'hr_full_name',
            'notify_number',
            'region',
            'region_unity',
            'state',
            'zip_code',
            'address',
            'address_number',
            'email',
            'activity',
            'type_of_activity',
            #   'inspections'
            'vat'
        ]

#detail for inspectors to make the checklist view
class StoreDetailSerializer(serializers.ModelSerializer):
    region_unity = serializers.StringRelatedField()
    region = serializers.StringRelatedField()
    state = serializers.StringRelatedField()
    zip_code = serializers.StringRelatedField()
    business = BusinessListSerializer()
    activity = ActivityDetailSerializer()
    type_of_activity = serializers.StringRelatedField()
    # health_regulator = HealthRegulatorListSerializer()
    # inspections= InspectionSerializer(many=True, read_only=True)

    class Meta:
        model = Store
        fields = [
            'id',
            'business',
            'category',
            'slug',
            # 'hr_full_name',
            'notify_number',
            'region',
            'region_unity',
            'state',
            'zip_code',
            'address',
            'address_number',
            'email',
            'activity',
            'type_of_activity',
            
            #   'inspections'
        ]
        extra_kwargs = {'url': {'lookup_field': 'slug'}}
