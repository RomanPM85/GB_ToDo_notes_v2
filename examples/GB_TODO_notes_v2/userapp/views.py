from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from django.contrib.auth.models import User
from .serializers import UserSerializer, UserSerializerWithFullName, UserSerializerStaff


class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_serializer_class(self):
        if self.request.version == '0.3':
            return UserSerializerStaff
        elif self.request.version == '0.2':
            return UserSerializerWithFullName
        return UserSerializer
