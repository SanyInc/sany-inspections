from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from rest_framework import routers

from accounts.views import InspectorViewSet, BusinessOwnerViewSet, HealthRegulatorViewSet, CustomerViewSet, ModeratorViewSet, AdminViewSet
from regions.views import ZipCodeViewSet, StateViewSet, RegionViewSet, RegionUnityViewSet
from businesses.views import BusinessViewSet, StoreViewSet
from checklists.views import ActivityViewSet, CategoryViewSet, QuestionViewSet
from inspections.views import CompletedViewSet

router = routers.DefaultRouter()
#businesses
router.register(r'stores', StoreViewSet, basename='stores')
router.register(r'businesses', BusinessViewSet, basename='businesses' )

#regions
router.register(r'zipcodes', ZipCodeViewSet)
router.register(r'states', StateViewSet)
router.register(r'region-unities', RegionUnityViewSet)
router.register(r'regions', RegionViewSet)

#users
router.register(r'inspectors', InspectorViewSet, basename='inspectors')
router.register(r'business-owners', BusinessOwnerViewSet, basename='business_owners')
router.register(r'health-regulators', HealthRegulatorViewSet, basename='health_regulators')
router.register(r'customers', CustomerViewSet, basename='customers')
router.register(r'moderators', ModeratorViewSet, basename='moderators')
router.register(r'admins', AdminViewSet, basename='admins')

#activities
router.register(r'questions', QuestionViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'activities', ActivityViewSet, basename='acivities')

#inspections
router.register(r'inspections', CompletedViewSet, basename='inspections')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('inspections.urls')),
    path('api/', include('checklists.urls')),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += path('__debug__/', include(debug_toolbar.urls)),