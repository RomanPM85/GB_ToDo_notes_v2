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


class ToDoAPIView(APIView):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]

    def get(self, request, format=None):
        pk = request.query_params.get('pk')
        todo = TODO.objects.all()
        if pk:
            todo = TODO.filter(id=pk)

        serializer = TODOModelSerializer(todo, many=True)
        return Response(serializer.data)

    # def post(self, request, format=None):
    #     pass

    # def delete(self, request, format=None):
    #     pass


# class FilterProjectModelViewSet(ModelViewSet):
#    queryset = Project.objects.all()
#    serializer_class = ProjectModelSerializer
#
#    def get_queryset(self):
#        name = self.request.query_params.get('name', '')
#        project = Project.objects.all()
#        if name:
#            project = project.filter(name__contains=name)
#        return project
