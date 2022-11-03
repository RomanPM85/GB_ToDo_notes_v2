from rest_framework.fields import ReadOnlyField
from rest_framework.serializers import ModelSerializer

from users.serializers import UserModelSerializer
from .models import Project, TODO


class ProjectModelSerializer(ModelSerializer):
    # user = UserModelSerializer()

    class Meta:
        model = Project
        fields = '__all__'
        # fields = ['title', 'linkGitHub', 'users']


class ProjectSerializerBase(ModelSerializer):
    # user = UserModelSerializer()

    class Meta:
        model = Project
        fields = '__all__'


class TODOModelSerializer(ModelSerializer):
    class Meta:
        model = TODO
        fields = '__all__'
