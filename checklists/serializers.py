from rest_framework import serializers
from .models import Question, Category, Choice, Activity, TypeOfActivity

class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ['id', 'number']

class QuestionSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ['id', 'order', 'title', 'slug', 'description', 'is_important', 'choices']

class CategorySerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True) 
    
    class Meta:
        model = Category
        fields = ['id', 'order', 'title', 'slug', 'questions']

class ActivityListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = [ 'title', 'slug', 'order']

class ActivityCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ['title', 'order']

class ActivityDetailSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)
    
    class Meta:
        model = Activity
        fields = ['id', 'order', 'title', 'slug', 'categories']
        extra_kwargs = {'url': {'lookup_field': 'slug'}}

class TypeOfActivityListSerializer(serializers.ModelSerializer):  
    class Meta:
        model = TypeOfActivity
        fields = ['id', 'title']
        extra_kwargs = {'url': {'lookup_field': 'slug'}}

class ActivityWithTypesSerializer(serializers.ModelSerializer):
    type_of_activities = TypeOfActivityListSerializer(many=True, read_only=True)
    
    class Meta:
        model = Activity
        fields = ['id', 'title', 'type_of_activities']
        extra_kwargs = {'url': {'lookup_field': 'slug'}}