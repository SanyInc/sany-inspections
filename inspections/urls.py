from django.urls import path
from .views import (InspectionCreateView, 
                    AnswerCreateView,                    
                    )

urlpatterns = [
    path('inspection/', InspectionCreateView.as_view(), name='inspection_create'),
    path('answers/', AnswerCreateView.as_view(), name='answer_create'),
]
