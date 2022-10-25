from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

# Create your views here.
from .serializers import ProjectModelSerializer, TODOModelSerializer
from .models import Project, TODO


class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer


class TODOModelViewSet(ModelViewSet):
    queryset = TODO.objects.all()
    serializer_class = TODOModelSerializer
