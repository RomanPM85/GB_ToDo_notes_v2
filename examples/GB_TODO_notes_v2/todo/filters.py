from django_filters import rest_framework as filters
from .models import Project, TODO


class ProjectFilter(filters.FilterSet):
    title = filters.CharFilter(lookup_expr='contains')

    class Meta:
        model = Project
        fields = ['title']


class ToDoFilter(filters.FilterSet):
    text = filters.CharFilter(lookup_expr='contains')

    class Meta:
        model = TODO
        fields = ['text', 'status']
