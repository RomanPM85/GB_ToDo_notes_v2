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


# class Query(ObjectType):
    # all_users = graphene.List(UserType)
    # all_project = graphene.List(ProjectType)
    # all_todo = graphene.List(TODOType)

    # def resolve_all_users(root, info):
    #     return User.objects.all()
    #
    # def resolve_all_project(root, info):
    #     return Project.objects.all()
    #
    # def resolve_all_todo(root, info):
    #     return TODO.objects.all()

    # all_users_by_id = graphene.Field(UserType, id=graphene.Int(required=True))
    # all_users_by_id = graphene.List(UserType, id=graphene.Int(required=False))

    # def resolve_all_users_by_id(root, info, id=None):
    #     if id:
    #         return User.objects.get(id=id)
    #     return User.objects.all()
    #
    # project_by_users = graphene.List(ProjectType, last_name=graphene.String(required=False))
    #
    # def resolve_project_by_users(root, info, last_name=None):
    #     if last_name:
    #         return Project.objects.filter(users__last_name=last_name)
    #     return Project.objects.all()


# class UserUpdateMutation(graphene.Mutation):
#     pass


class UserCreateMutation(graphene.Mutation):
    class Arguments:
        user_name = graphene.String()
        first_name = graphene.String()
        last_name = graphene.String()
        email = graphene.String()

    user = graphene.Field(UserType)

    @classmethod
    def mutate(cls, root, info, user_name, first_name, last_nam, email):
        user = User(user_name=user_name, first_name=first_name, last_nam=last_nam, email=email)
        user.save()
        return UserCreateMutation(user=user)


# class UserDeleteMutation(graphene.Mutation):
#     pass


class Mutations(ObjectType):
    # update_user = UserUpdateMutation.Field()
    create_user = UserCreateMutation.Field()
    # delete_user = UserDeleteMutation.Field()


# schema = graphene.Schema(query=Query)
schema = graphene.Schema(mutation=Mutations)
