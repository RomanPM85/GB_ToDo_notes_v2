from rest_framework.fields import ReadOnlyField
from rest_framework.serializers import ModelSerializer

from .models import Project, TODO


class ProjectModelSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
        # fields = ['title', 'linkGitHub', 'users']


class TODOModelSerializer(ModelSerializer):
    class Meta:
        model = TODO
        fields = '__all__'
