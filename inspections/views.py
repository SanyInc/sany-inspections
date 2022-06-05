from django.shortcuts import render
from rest_framework import filters, viewsets, generics
from accounts.models import Inspector
from .models import Complete
from .pagination import MyPageNumberPagination
from .serializers import CompleteCreateSerializer, CompletedListSerializer, CompletedDetailSerializer, InspectionCreateSerializer, AnswerCreateSerializer

# Create your views here.
class InspectionCreateView(generics.CreateAPIView):
    serializer_class = InspectionCreateSerializer

    def perform_create(self, serializar):
        user = Inspector.objects.get(user=self.request.user)
        serializar.save(inspector=user)

class AnswerCreateView(generics.CreateAPIView):
    serializer_class = AnswerCreateSerializer

class CompletedViewSet(viewsets.ModelViewSet):
    pagination_class = MyPageNumberPagination
    filter_backends = (filters.SearchFilter, )
    search_fields = ['inspection__store__business__vat']
    lookup_field = 'inspection__uuid'
    http_method_names = ['get', 'post']

    def get_serializer_class(self):
        if self.action == 'list':
            return CompletedListSerializer
        elif self.action == 'retrieve':
            return CompletedDetailSerializer
        return CompleteCreateSerializer

    def get_queryset(self):
        queryset = Complete.objects.select_related('inspection__store__business__owner__user', 
                                                'inspection__store__region', 
                                                'inspection__store__region_unity',
                                                'inspection__store__state',
                                                'inspection__store__zip_code',
                                                'inspection__store__activity',
                                                'inspection__store__type_of_activity',
                                                'inspection__store__healthregulator__user',
                                                'inspection__inspector__user',
                                                'inspection__inspector__partner__user')
        queryset_detail = queryset.prefetch_related('inspection__answers__question')

        if self.request.user.role == 'Admin':          
            if self.action == 'list':
                return queryset
            elif self.action == 'retrieve':
                return queryset_detail

        elif self.request.user.role == 'Inspector':          
            if self.action == 'list':
                return queryset.filter(inspection__inspector__user=self.request.user)
            elif self.action == 'retrieve':
                return queryset_detail.filter(inspection__inspector__user=self.request.user)

        elif self.request.user.role == 'Business Owner':
            if self.action == 'list':
                return queryset.filter(inspection__store__business__owner__user=self.request.user)
            elif self.action == 'retrieve':
                return queryset_detail.filter(inspection__store__business__owner__user=self.request.user)

        elif self.request.user.role == 'Health Regulator':
            if self.action == 'list':
                return queryset.filter(inspection__store__healthregulator__user=self.request.user)
            elif self.action == 'retrieve':
                return queryset_detail.filter(inspection__store__healthregulator__user=self.request.user)
