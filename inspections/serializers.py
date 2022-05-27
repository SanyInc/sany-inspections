from rest_framework import serializers
from .models import Inspection, Answer, Complete
from accounts.serializers import InspectorDetailSerializer
from businesses.serializers import StoreListSerializer

class AnswerCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('question', 'body', 'inspection', 'comment', 'timestamp')

class AnswerDetailSerializer(serializers.ModelSerializer):
    question = serializers.StringRelatedField()

    class Meta:
        model = Answer
        fields = ('question', 'body', 'comment', 'timestamp')

class InspectionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inspection
        fields = '__all__'

class InspectionListSeriarizer(serializers.ModelSerializer):
    store = StoreListSerializer(read_only=True)
    inspector = InspectorDetailSerializer(read_only=True)
    
    class Meta:
        model = Inspection
        fields = ('store', 'inspector',
                  'uuid', 'date_created')

class InspectionDetailSeriarizer(serializers.ModelSerializer):
    store = StoreListSerializer(read_only=True)
    inspector = InspectorDetailSerializer(read_only=True)
    answers = AnswerDetailSerializer(many=True, read_only=True)
    
    class Meta:
        model = Inspection
        fields = ('store', 'inspector',
                  'uuid', 'date_created', 'answers')

class CompleteCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complete
        fields = ('inspection', 'completed', 'score')

class CompletedListSerializer(serializers.ModelSerializer):
    inspection = InspectionListSeriarizer(read_only=True)

    class Meta:
        model = Complete
        fields = ('completed', 'score', 'inspection')

class CompletedDetailSerializer(serializers.ModelSerializer):
    inspection = InspectionDetailSeriarizer(read_only=True)

    class Meta:
        model = Complete
        fields = '__all__'