from django.urls import path

from .views import ActivityWithTypesView

urlpatterns = [
    path('activity/', ActivityWithTypesView.as_view(), name='activity_list'),
    ]
