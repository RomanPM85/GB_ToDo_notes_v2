from graphene import ObjectType
from graphene_django import DjangoObjectType
from users.models import User
from todo.models import Project, TODO
import graphene


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = '__all__'


class ProjectType(DjangoObjectType):
    class Meta:
        model = Project
        fields = '__all__'


class TODOType(DjangoObjectType):
    class Meta:
        model = TODO
        fields = '__all__'


class Query(ObjectType):
    all_users = graphene.List(UserType)
    all_project = graphene.List(ProjectType)
    all_todo = graphene.List(TODOType)

    def resolve_all_users(root, info):
        return User.objects.all()

    def resolve_all_project(root, info):
        return Project.objects.all()

    def resolve_all_todo(root, info):
        return TODO.objects.all()


schema = graphene.Schema(query=Query)
