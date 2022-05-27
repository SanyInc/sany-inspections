from rest_framework import viewsets, generics
from .models import Question, Category, Activity, TypeOfActivity
from .serializers import QuestionSerializer, CategorySerializer, ActivityCreateSerializer, ActivityDetailSerializer, ActivityWithTypesSerializer, ActivityListSerializer
from .pagination import MyPageNumberPagination

# Create your views here.
class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.select_related('category').prefetch_related('choices')
    serializer_class = QuestionSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.select_related('activity').prefetch_related('questions__choices')
    serializer_class = CategorySerializer

class ActivityViewSet(viewsets.ModelViewSet):
    pagination_class = MyPageNumberPagination
    lookup_field = 'slug'
    http_method_names = ['get', 'post']

    def get_serializer_class(self):
        if self.action == 'list':
            return ActivityListSerializer
        elif self.action == 'retrieve':
            return ActivityDetailSerializer
        return ActivityCreateSerializer

    def get_queryset(self):
        queryset = Activity.objects.all()
        queryset_detail = Activity.objects.prefetch_related('categories__questions__choices')

        # if self.request.user.role in ('Inspector' or 'Admin' or 'Moderator'):          
        if self.action == 'list':
            return queryset
        elif self.action == 'retrieve':
            return queryset_detail
    #     elif self.request.user.role == 'Admin':          
    #         if self.action == 'list':
    #             return queryset
    #         elif self.action == 'retrieve':
    #             return queryset_detail

class ActivityWithTypesView(generics.ListAPIView):
    queryset = Activity.objects.prefetch_related('type_of_activities')
    serializer_class = ActivityWithTypesSerializer



