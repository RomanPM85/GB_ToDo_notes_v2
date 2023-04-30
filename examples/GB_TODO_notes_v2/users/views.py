from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

# Create your views here.

# Create your views here.
from .serializers import UserModelSerializer, UserModelSerializerBase
from .models import User


class UserModelViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer

    def get_serializer_class(self):
        if self.request.version == '2.0':
            return UserModelSerializerBase
        return UserModelSerializer
