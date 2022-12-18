from django.shortcuts import render
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

# Create your views here.
from .serializers import ProjectModelSerializer, TODOModelSerializer, ProjectSerializerBase
from .models import Project, TODO


class ProjectModelViewSet(ModelViewSet):
    # permission_classes = [permissions.IsAuthenticated]
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer

    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return ProjectModelSerializer
        return ProjectSerializerBase


class TODOModelViewSet(ModelViewSet):
    # permission_classes = [permissions.IsAuthenticated]
    queryset = TODO.objects.all()
    serializer_class = TODOModelSerializer
