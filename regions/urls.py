from rest_framework import routers
from django.urls import path, include

from regions.views import ZipCodeViewSet, StateViewSet, RegionViewSet, RegionUnityViewSet

router = routers.DefaultRouter()
router.register(r'zipcodes', ZipCodeViewSet)
router.register(r'states', StateViewSet)
router.register(r'region-unities', RegionUnityViewSet)
router.register(r'regions', RegionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]