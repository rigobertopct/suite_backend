import graphene
from django.contrib.auth.models import Group
from django.db.models import Q
from graphene_django import DjangoObjectType

from Espannol.seguridad.models import ExtendUser


class UserType(DjangoObjectType):
    class Meta:
        model = ExtendUser
        fields = '__all__'


class GroupType(DjangoObjectType):
    class Meta:
        model = Group
        fields = '__all__'


class Query(graphene.ObjectType):
    group_by_user = graphene.String(user_id=graphene.Int())
    usuarios = graphene.List(UserType, name=graphene.String())
    grupos = graphene.List(GroupType)
    user_by_id = graphene.Field(UserType, id=graphene.Int())

    def resolve_group_by_user(self, info, user_id):

        if ExtendUser.objects.filter(id=user_id).exists():
            user = ExtendUser.objects.get(id=user_id)
            return user.groups.name if user.groups is not None else "None"
        else:
            return "None"

    def resolve_usuarios(self, info, name):
        if name == "":
            return ExtendUser.objects.all()
        else:
            return ExtendUser.objects.filter(
                Q(username__icontains=name) |
                Q(first_name__icontains=name) |
                Q(last_name=name) |
                Q(email__icontains=name)
            )

    def resolve_grupos(self, info):
        return Group.objects.all()

    def resolve_user_by_id(self, info, id):
        return ExtendUser.objects.get(id=id)
