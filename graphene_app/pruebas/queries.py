from django.db.models import Q

from graphene_app.deportista.queries import *
from Espannol.pruebas.models import *


class RastType(DjangoObjectType):
    class Meta:
        model = Rast
        fields = '__all__'


class CarlsonType(DjangoObjectType):
    class Meta:
        model = Carlson
        fields = '__all__'


class LugarType(DjangoObjectType):
    class Meta:
        model = Lugar
        fields = '__all__'


class ProvinciaType(DjangoObjectType):
    class Meta:
        model = Provincia
        fields = '__all__'


class PruebaType(DjangoObjectType):
    class Meta:
        model = Prueba
        fields = '__all__'


class Query(graphene.ObjectType):
    rast = graphene.List(RastType)
    carlson = graphene.List(CarlsonType)
    lugares = graphene.List(LugarType, name=graphene.String())
    provincias = graphene.List(ProvinciaType)
    pruebas = graphene.List(PruebaType, name=graphene.String())

    verificar_pruebas_rast = graphene.Boolean(id=graphene.ID())
    verificar_pruebas_carlson = graphene.Boolean(id=graphene.ID())

    rast_prueba = graphene.Field(RastType, id=graphene.ID())
    carlson_prueba = graphene.Field(CarlsonType, id=graphene.ID())

    def resolve_rast(self, info):
        return Rast.objects.all()

    def resolve_carlson(self, info):
        return Carlson.objects.all()

    def resolve_lugares(self, info, name):
        if name == "":
            return Lugar.objects.all()
        else:
            return Lugar.objects.filter(nombre__icontains=name)

    def resolve_provincias(self, info):
        return Provincia.objects.all()

    def resolve_pruebas(self, info, name):
        if name == "":
            return Prueba.objects.all()
        else:
            return Prueba.objects.filter(
                Q(deportista__nombre__icontains=name) |
                Q(deportista__disciplina__deporte__nombre__icontains=name) |
                Q(deportista__sexo__icontains=name)
            )

    def resolve_verificar_pruebas_rast(self, info, id):
        return Rast.objects.filter(prueba_id=id)

    def resolve_verificar_pruebas_carlson(self, info, id):
        return Carlson.objects.filter(prueba_id=id)

    def resolve_rast_prueba(self, info, id):
        return Rast.objects.filter(prueba_id=id).first()

    def resolve_carlson_prueba(self, info, id):
        return Carlson.objects.filter(prueba_id=id).first()
