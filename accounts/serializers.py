from urllib import request
from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from .models import User, HealthRegulator, BusinessOwner, Inspector, Customer, Moderator, Admin

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']

class PartnerSeralizer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Inspector
        fields = ['user']

class AuthTokenSerializer(serializers.Serializer):
    email = serializers.CharField(
        label=_("Email"),
        write_only=True
    )
    password = serializers.CharField(
        label=_("Password"),
        style={'input_type': 'password'},
        trim_whitespace=False,
        write_only=True
    )
    token = serializers.CharField(
        label=_("Token"),
        read_only=True
    )

class InspectorLoginSerializer(AuthTokenSerializer):
    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(request=self.context.get('request'),
                                email=email, password=password)
            if not user:
                msg = _('There isn\'t account with these credentials, or you have writen them wrong')
                raise serializers.ValidationError(msg, code='authorization')
            elif not user.role=='Inspector':
                msg = _('You don\'t have access here with these credentials.')
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = _('Must include "email" and "password".')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs

class BusinessOwnerLoginSerializer(AuthTokenSerializer):
    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(request=self.context.get('request'),
                                email=email, password=password)
            if not user:
                msg = _('Unable to log in. There isn\'t account with these credentials, or you have writen them wrong')
                raise serializers.ValidationError(msg, code='authorization')
            elif not user.role=='Business Owner':
                msg = _('You don\'t have access here with these credentials.')
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = _('Must include "email" and "password".')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs

class HealthRegulatorLoginSerializer(AuthTokenSerializer):
    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(request=self.context.get('request'),
                                email=email, password=password)
            if not user:
                msg = _('Unable to log in. There isn\'t account with these credentials, or you have writen them wrong')
                raise serializers.ValidationError(msg, code='authorization')
            elif not user.role=='Health Regulator':
                msg = _('You don\'t have access here with these credentials.')
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = _('Must include "email" and "password".')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs

class CustomerLoginSerializer(AuthTokenSerializer):
    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(request=self.context.get('request'),
                                email=email, password=password)
            if not user:
                msg = _('Unable to log in. There isn\'t account with these credentials, or you have writen them wrong')
                raise serializers.ValidationError(msg, code='authorization')
            elif not user.role=='Customer':
                msg = _('You don\'t have access here with these credentials.')
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = _('Must include "email" and "password".')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs

class ModeratorLoginSerializer(AuthTokenSerializer):
    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(request=self.context.get('request'),
                                email=email, password=password)
            if not user:
                msg = _('Unable to log in. There isn\'t account with these credentials, or you have writen them wrong')
                raise serializers.ValidationError(msg, code='authorization')
            elif not user.role=='Moderator':
                msg = _('You don\'t have access here with these credentials.')
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = _('Must include "email" and "password".')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs

class AdminLoginSerializer(AuthTokenSerializer):
    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(request=self.context.get('request'),
                                email=email, password=password)
            if not user:
                msg = _('Unable to log in. There isn\'t account with these credentials, or you have writen them wrong')
                raise serializers.ValidationError(msg, code='authorization')
            elif not user.role=='Admin':
                msg = _('You don\'t have access here with these credentials.')
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = _('Must include "email" and "password".')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        style={'input_type': 'password'}, write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(
        style={'input_type': 'password'}, write_only=True, required=True)

    class Meta:
        model = User
        fields = ('email', 'password', 'password2', 'first_name', 'last_name')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."})
        return attrs

class InspectorCreateSerializer(RegisterSerializer):
    def create(self, validated_data):
        user = User.objects.create_inspector(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            created_by=self.request.user
        )
        user.set_password(validated_data['password'])
        user.save()

        return user

class InspectorListSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    partner = PartnerSeralizer()
    region_unity = serializers.StringRelatedField()
    region = serializers.StringRelatedField()
    state = serializers.StringRelatedField()
    zip_code = serializers.StringRelatedField()

    class Meta:
        model = Inspector
        fields = '__all__'

class InspectorDetailSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    partner = PartnerSeralizer()

    class Meta:
        model = Inspector
        fields = ['user', 'partner']

class CustomerCreateSerializer(RegisterSerializer):
    def create(self, validated_data):
        user = User.objects.create_customer(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            created_by=validated_data['created_by']
        )
        user.set_password(validated_data['password'])
        user.save()

        return user

class CustomerListSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Customer
        fields = ['user']

class BusinessOwnerCreateSerializer(RegisterSerializer):
    def create(self, validated_data):
        user = User.objects.create_business_owner(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        user.set_password(validated_data['password'])
        user.save()

        return user

class BusinessOwnerListSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = BusinessOwner
        fields = ['user']

class HealthRegulatorCreateSerializer(RegisterSerializer):
    def create(self, validated_data):
        user = User.objects.create_health_regulator(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            created_by=validated_data['created_by']
        )
        user.set_password(validated_data['password'])
        user.save()

        return user

class HealthRegulatorListSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = HealthRegulator
        fields = ['user']

class ModeratorCreateSerializer(RegisterSerializer):
    def create(self, validated_data):
        user = User.objects.create_moderator(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            created_by=validated_data['created_by']
        )
        user.set_password(validated_data['password'])
        user.save()

        return user

class ModeratorListSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Moderator
        fields = ['user']

class AdminCreateSerializer(RegisterSerializer):
    def create(self, validated_data):
        user = User.objects.create_superuser(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            created_by=validated_data['created_by']
        )
        user.set_password(validated_data['password'])
        user.save()

        return user

class AdminListSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Admin
        fields = ['user']