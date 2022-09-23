from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

# Create your views here.

# Create your views here.
from .serializers import UserModelSerializer
from .models import User


class UserModelViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
