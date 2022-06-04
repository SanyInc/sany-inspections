from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from rest_framework import routers, permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from accounts.views import InspectorViewSet, BusinessOwnerViewSet, HealthRegulatorViewSet, CustomerViewSet, ModeratorViewSet, AdminViewSet
from regions.views import ZipCodeViewSet, StateViewSet, RegionViewSet, RegionUnityViewSet
from businesses.views import BusinessViewSet, StoreViewSet
from checklists.views import ActivityViewSet, CategoryViewSet, QuestionViewSet
from inspections.views import CompletedViewSet

schema_view = get_schema_view(
   openapi.Info(
      title="Inspections API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.sany-inc.com/policies/terms/",
      contact=openapi.Contact(email="sany.inspections@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

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
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc')
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += path('__debug__/', include(debug_toolbar.urls)),