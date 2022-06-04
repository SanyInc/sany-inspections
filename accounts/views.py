from rest_framework import viewsets

from . import mixins

from .models import User, HealthRegulator, BusinessOwner, Inspector, Customer, Moderator, Admin
from .serializers import (InspectorLoginSerializer,
                          InspectorCreateSerializer, 
                          InspectorListSerializer, 
                          CustomerCreateSerializer,
                          CustomerLoginSerializer, 
                          CustomerListSerializer,
                          BusinessOwnerCreateSerializer,
                          BusinessOwnerListSerializer,
                          BusinessOwnerLoginSerializer,
                          HealthRegulatorLoginSerializer,
                          HealthRegulatorCreateSerializer,
                          HealthRegulatorListSerializer,
                          ModeratorListSerializer,
                          ModeratorCreateSerializer,
                          ModeratorLoginSerializer,
                          AdminLoginSerializer,
                          AdminListSerializer,
                          AdminCreateSerializer)


class InspectorViewSet(viewsets.ModelViewSet, mixins.LoginMixin):
    queryset = Inspector.objects.select_related('user', 'partner__user', 'region', 'region_unity', 'state', 'zip_code')

    def get_serializer_class(self):
        if self.action == 'list':
            return InspectorListSerializer
        elif self.action == 'login':
            return InspectorLoginSerializer
        return InspectorCreateSerializer

    # def perform_create(self, serializer):       
    #     serializer.save(created_by=self.request.user)

class BusinessOwnerViewSet(viewsets.ModelViewSet, mixins.LoginMixin):
    queryset = BusinessOwner.objects.select_related('user')

    def get_serializer_class(self):
        if self.action == 'list':
            return BusinessOwnerListSerializer
        elif self.action == 'login':
            return BusinessOwnerLoginSerializer
        return BusinessOwnerCreateSerializer

class HealthRegulatorViewSet(viewsets.ModelViewSet, mixins.LoginMixin):
    queryset = HealthRegulator.objects.select_related('user')

    def get_serializer_class(self):
        if self.action == 'list':
            return HealthRegulatorListSerializer
        elif self.action == 'login':
            return HealthRegulatorLoginSerializer
        return HealthRegulatorCreateSerializer

    def perform_create(self, serializer):       
        serializer.save(created_by=self.request.user)

class CustomerViewSet(viewsets.ModelViewSet, mixins.LoginMixin):
    queryset = Customer.objects.select_related('user')

    def get_serializer_class(self):
        if self.action == 'list':
            return CustomerListSerializer
        elif self.action == 'login':
            return CustomerLoginSerializer
        return CustomerCreateSerializer

class ModeratorViewSet(viewsets.ModelViewSet, mixins.LoginMixin):
    queryset = Moderator.objects.select_related('user')

    def get_serializer_class(self):
        if self.action == 'list':
            return ModeratorListSerializer
        elif self.action == 'login':
            return ModeratorLoginSerializer
        return ModeratorCreateSerializer

class AdminViewSet(viewsets.ModelViewSet, mixins.LoginMixin):
    queryset = Admin.objects.select_related('user')

    def get_serializer_class(self):
        if self.action == 'list':
            return AdminListSerializer
        elif self.action == 'login':
            return AdminLoginSerializer
        return AdminCreateSerializer