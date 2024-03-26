import graphene
from django.contrib.auth.models import Group
from graphene import Mutation

from Espannol.seguridad.models import ExtendUser


class CrearUsuario(Mutation):
    class Arguments:
        nombre = graphene.String()
        apellidos = graphene.String()
        usuario = graphene.String()
        email = graphene.String()
        password = graphene.String()
        grupo = graphene.Int()

    error = graphene.String()
    success = graphene.Boolean()

    def mutate(self, info, nombre, apellidos, usuario, email, password, grupo):
        try:
            group = Group.objects.get(id=grupo)
            user = ExtendUser.objects.create(email=email, first_name=nombre, last_name=apellidos, username=usuario)
            user.groups = group
            user.set_password(password)
            user.save()
            return CrearUsuario(error=None, success=True)
        except Exception as e:
            return CrearUsuario(error=str(e), success=False)


class ActualizarUsuario(Mutation):
    class Arguments:
        nombre = graphene.String()
        apellidos = graphene.String()
        usuario = graphene.String()
        email = graphene.String()
        id = graphene.Int()

    error = graphene.String()
    success = graphene.Boolean()

    def mutate(self, info, nombre, apellidos, usuario, email, id):
        try:
            user = ExtendUser.objects.get(id=id)
            user.email = email
            user.first_name = nombre
            user.last_name = apellidos
            user.username = usuario
            user.save()
            return ActualizarUsuario(error=None, success=True)
        except Exception as e:
            return ActualizarUsuario(error=str(e), success=False)


class ActualizarPassword(Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        password = graphene.String(required=True)
        new_password = graphene.String(required=True)

    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, password, new_password, id):
        try:
            user = ExtendUser.objects.get(id=id)
            if user.check_password(password):
                user.set_password(new_password)
                user.save()
                return ActualizarPassword(success=True, error=None)
            else:
                return ActualizarPassword(success=False, error="Contraseña anterior incorrecta")
        except Exception as e:
            return ActualizarPassword(error=str(e), success=False)


class Mutation(graphene.ObjectType):
    crearUsuario = CrearUsuario.Field()
    actualizarUsuario = ActualizarUsuario.Field()
    actualizarPassword = ActualizarPassword.Field()
