from django.http import Http404
from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes, action
from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin,\
    DestroyModelMixin
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, ViewSet, GenericViewSet
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView, \
    get_object_or_404

from todo.models import Project, TODO
from todo.serializers import ProjectModelSerializer, TODOModelSerializer
from users.models import User
from users.serializers import UserModelSerializer


class UserCustomViewSet(ListModelMixin, UpdateModelMixin, RetrieveModelMixin, GenericViewSet):
    """
    Custom ViewSet для модели User добавляем возможность просмотра списка и каждого пользователя в
    отдельности, и возможность вносить изменения.
    """
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]


class ToDoListAPIView(APIView):
    """
    Список всех созданных заметок к проекту и возможность
    создать новую заметку через метод POST.
    """
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]

    def get(self, request, format=None):
        todo = TODO.objects.all()
        serializer = TODOModelSerializer(todo, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TODOModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ToDoDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return TODO.objects.get(pk=pk)
        except TODO.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        todo = self.get_object(pk)
        serializer = TODOModelSerializer(todo)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        todo = self.get_object(pk)
        serializer = TODOModelSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        todo = self.get_object(pk)
        serializer = TODOModelSerializer(todo, data={'status': 'с'}, partial=True)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
