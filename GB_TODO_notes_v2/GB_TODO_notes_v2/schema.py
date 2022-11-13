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

    users_by_id = graphene.Field(UserType, id=graphene.Int(required=True))
    # all_users_by_id = graphene.List(UserType, id=graphene.Int(required=False))

    def resolve_users_by_id(self, info, id):
        try:
            return User.objects.get(id=id)
        except User.DoesNotExist:
            return None

    project_by_users = graphene.List(ProjectType, last_name=graphene.String(required=False))

    def resolve_project_by_users(root, info, last_name=None):
        if last_name:
            return Project.objects.filter(users__last_name=last_name)
        return Project.objects.all()


class UserCreateMutation(graphene.Mutation):
    class Arguments:
        user_name = graphene.String()
        first_name = graphene.String()
        last_name = graphene.String()
        email = graphene.String()

    user = graphene.Field(UserType)

    @classmethod
    def mutate(cls, root, info, **kwargs):
        # user = User.objects.create(user_name, first_name, last_name, email)
        user = User.objects.create(**kwargs)
        # user.user_name = user_name
        # user.first_name = first_name
        # user.last_name = last_name
        # user.email = email
        user.save()
        return cls(user=user)


class UserUpdateMutation(graphene.Mutation):
    class Arguments:
        user_name = graphene.String()
#         first_name = graphene.String()
#         last_name = graphene.String()
#         email = graphene.String()
        id = graphene.ID()

    user = graphene.Field(UserType)

    @classmethod
    def mutate(cls, root, info, user_name, id):
        user = User.objects.get(pk=id)
        user.user_name = user_name
        user.save()
        return UserUpdateMutation(user=user)


class UserDeleteMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    user = graphene.List(UserType)

    @classmethod
    def mutate(cls, root, info, **kwargs):
        User.objects.get(id=kwargs.get('id')).delete()
        return cls(user=User.objects.all())


class Mutations(ObjectType):
    update_user = UserUpdateMutation.Field()
    create_user = UserCreateMutation.Field()
    delete_user = UserDeleteMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutations)
