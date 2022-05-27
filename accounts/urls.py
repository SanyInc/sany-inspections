from rest_framework import routers
from django.urls import path, include
from .views import InspectorViewSet, BusinessOwnerViewSet, HealthRegulatorViewSet, CustomerViewSet, AdminViewSet, ModeratorViewSet

router = routers.DefaultRouter()
router.register(r'inspectors', InspectorViewSet, basename='inspectors')
router.register(r'business-owners', BusinessOwnerViewSet, basename='business_owners')
router.register(r'health-regulators', HealthRegulatorViewSet, basename='health_regulators')
router.register(r'customers', CustomerViewSet, basename='customers')
router.register(r'moderators', ModeratorViewSet, basename='moderators')
router.register(r'admins', AdminViewSet, basename='admins')


urlpatterns = [
    path('', include(router.urls)),
]