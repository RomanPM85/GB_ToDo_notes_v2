from graphene import ObjectType
from graphene_django import DjangoObjectType
from users.models import User
from todo.models import Project, TODO
import graphene


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = '__all__'


class Query(ObjectType):
    all_users = graphene.List(UserType)

    def resolve_all_users(root, info):
        return User.objects.all()


schema = graphene.Schema(query=Query)
