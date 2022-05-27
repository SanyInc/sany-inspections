from rest_framework import viewsets
from .models import ZipCode, State, Region, RegionUnity
from .serializers import ZipCodeSerializer, StateSerializer, RegionSerializer, RegionUnitySerializer

# Create your views here.
class ZipCodeViewSet(viewsets.ModelViewSet):
    queryset = ZipCode.objects.all()
    serializer_class = ZipCodeSerializer

class StateViewSet(viewsets.ModelViewSet):
    queryset = State.objects.prefetch_related('zip_codes')
    serializer_class = StateSerializer

class RegionUnityViewSet(viewsets.ModelViewSet):
    queryset = RegionUnity.objects.prefetch_related('states__zip_codes')
    serializer_class = RegionUnitySerializer

class RegionViewSet(viewsets.ModelViewSet):
    queryset = Region.objects.prefetch_related('region_unities__states__zip_codes')
    serializer_class = RegionSerializer