from rest_framework import filters, viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated

from accounts.models import BusinessOwner, Admin, Inspector
from businesses.models import Business, Store
from businesses.pagination import MyPageNumberPagination
from businesses.serializers import (BusinessCreateSerializer, BusinessDetailSerializer, BusinessListSerializer,
                                    StoreCreateSerializer, StoreDetailSerializer, StoreListSerializer)

class BusinessViewSet(viewsets.ModelViewSet):
    filter_backends = (filters.SearchFilter, )
    http_method_names = ['get']
    # http_method_names = ['get', 'post']
    lookup_field = 'slug'
    pagination_class = MyPageNumberPagination
    search_fields = ['vat']  
    
    def get_serializer_class(self):
        if self.action == 'list':
            return BusinessListSerializer
        elif self.action == 'retrieve':
            return BusinessDetailSerializer
        return BusinessCreateSerializer

    def get_queryset(self):
        queryset = Business.objects.select_related('owner__user__auth_token')
        queryset_detail = queryset.prefetch_related('stores__region',
                                                    'stores__region_unity',
                                                    'stores__state',
                                                    'stores__zip_code',
                                                    'stores__activity',
                                                    'stores__type_of_activity',
                                                    'stores__healthregulator__user__auth_token' )

        if self.request.user.role in ('Admin' or 'Moderator' or 'Inspector'):          
            if self.action == 'list':
                return queryset
            elif self.action == 'retrieve':
                return queryset_detail


        elif self.request.user.role == 'Business Owner':          
            if self.action == 'list':
                return queryset.filter(owner__user=self.request.user)
            elif self.action == 'retrieve':
                return queryset_detail.filter(owner__user=self.request.user)

    def perform_create(self, serializer):
        user = BusinessOwner.objects.get(user=self.request.user)
        serializer.save(owner=user)

class StoreViewSet(viewsets.ModelViewSet):
    filter_backends = [filters.SearchFilter, ]
    search_fields = ['region__title', 'region_unity__title', 'activity__title', 'state__title', 'notify_number', 'business__vat']
    pagination_class = MyPageNumberPagination
    http_method_names = ['get']
    # http_method_names = ['get', 'post']
    lookup_field = 'slug'

    def get_serializer_class(self):
        if self.action == 'list':
            return StoreListSerializer
        elif self.action == 'retrieve':
            return StoreDetailSerializer
        return StoreCreateSerializer

    def get_queryset(self):
        queryset = Store.objects.select_related('business__owner__user',
                                                'healthregulator__user',
                                                'region',
                                                'region_unity',
                                                'state',
                                                'zip_code',
                                                'activity',
                                                'type_of_activity')
        queryset_detail = queryset.prefetch_related('activity__categories__questions__choices')

        if self.request.user.role in ('Admin' or 'Moderator'):          
            if self.action == 'list':
                return queryset
            elif self.action == 'retrieve':
                return queryset_detail

        elif self.request.user.role == 'Inspector':
            if self.action == 'list':
                return queryset.filter(region=self.request.user.inspector.region)
            elif self.action == 'retrieve':
                return queryset_detail.filter(region=self.request.user.inspector.region)

        elif self.request.user.role == 'Business Owner':          
            if self.action == 'list':
                return queryset.filter(business__owner__user=self.request.user)
            elif self.action == 'retrieve':
                return queryset_detail.filter(business__owner__user=self.request.user)

        elif self.request.user.role == 'Health Regulator':
            if self.action == 'list':
                return queryset.filter(healthregulator__user=self.request.user)
            elif self.action == 'retrieve':
                return queryset.prefetch_related('inspection__answers__question').filter(healthregulator__user=self.request.user)