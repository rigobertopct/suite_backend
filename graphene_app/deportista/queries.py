import graphene
from graphene_django import DjangoObjectType

from Deportes.models import Deporte, Disciplina
from deportista.models import Deportista, DeportistaDisciplina
from seguridad.models import Provincia


class DeportistaType(DjangoObjectType):
    class Meta:
        model = Deportista
        fields = '__all__'


class DeporteType(DjangoObjectType):
    class Meta:
        model = Deporte
        fields = '__all__'


class DisciplinaType(DjangoObjectType):
    class Meta:
        model = Disciplina
        fields = '__all__'


class DeportistaDisciplinaType(DjangoObjectType):
    class Meta:
        model = DeportistaDisciplina
        fields = '__all__'


class ProvinciaType(DjangoObjectType):
    class Meta:
        model = Provincia
        fields = '__all__'


class Query(graphene.ObjectType):
    deportistas = graphene.List(DeportistaType, name=graphene.String())
    deportes = graphene.List(DeporteType, name=graphene.String(), idioma=graphene.String())
    disciplinas = graphene.List(DisciplinaType, name=graphene.String(), idioma=graphene.String())

    def resolve_deportistas(self, info, name):
        if name == "":
            return Deportista.objects.all()
        else:
            return Deportista.objects.filter(nombre__icontains=name)

    def resolve_disciplinas(self, info, name, idioma):
        if name == "":
            return Disciplina.objects.all().filter(idioma=idioma)
        else:
            return Disciplina.objects.filter(nombre__icontains=name).filter(idioma=idioma)

    def resolve_deportes(self, info, name, idioma):
        if name == "":
            return Deporte.objects.all().filter(idioma=idioma)
        else:
            return Deporte.objects.filter(nombre__icontains=name).filter(idioma=idioma)
