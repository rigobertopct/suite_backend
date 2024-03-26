import graphene
from django.db.models import Q
from django.utils.translation import activate
from graphene_django import DjangoObjectType

from Espannol.boxeo.models import Combate
from graphene_app.boxeo.queries import CombateType
from Espannol.nomencladores.models import TipoEvento, Pais, Evento


class TipoEventoType(DjangoObjectType):
    class Meta:
        model = TipoEvento
        fields = '__all__'


class PaisType(DjangoObjectType):
    class Meta:
        model = Pais
        fields = '__all__'


class EventoType(DjangoObjectType):
    class Meta:
        model = Evento
        fields = '__all__'


class Query(graphene.ObjectType):
    tiposE = graphene.List(TipoEventoType, name=graphene.String())
    paises = graphene.List(PaisType, name=graphene.String())
    eventos = graphene.List(EventoType, name=graphene.String())
    cant_nacionales = graphene.Int()
    cant_internacionales = graphene.Int()
    annos_eventos = graphene.List(graphene.Int)
    eventos_by_year = graphene.List(EventoType, year=graphene.Int())
    combates_by_eventos = graphene.List(CombateType, evento=graphene.Int())

    def resolve_paises(self, info, name):
        if name == "":
            return Pais.objects.all()
        else:
            return Pais.objects.filter(
                Q(pais__icontains=name) | Q(siglas__icontains=name)

            )

    def resolve_tiposE(self, info, name):
        if name == "":
            return TipoEvento.objects.all()
        else:
            return TipoEvento.objects.filter(tipo__icontains=name)

    def resolve_eventos(self, info, name):
        if name == "":
            return Evento.objects.all()
        else:
            return Evento.objects.filter(
                Q(nombre__icontains=name) | Q(pais__pais__icontains=name) | Q(
                    reglamento__tipo__icontains=name) | Q(tipoevento__tipo__icontains=name)

            )

    def resolve_cant_nacionales(self, info):
        return Evento.objects.filter(pais__pais__icontains="Cuba").count()

    def resolve_cant_internacionales(self, info):
        return Evento.objects.all().count() - Evento.objects.filter(pais__pais__icontains="Cuba").count()

    def resolve_annos_eventos(self, info):
        anos_unicos = Evento.objects.values_list('anno', flat=True).distinct()
        return anos_unicos

    def resolve_eventos_by_year(self, info, year=None):
        if year == 0:
            return Evento.objects.all()
        else:
            return Evento.objects.filter(anno=year)

    def resolve_combates_by_eventos(self, info, evento):
        if evento == 0:
            return Combate.objects.all()
        else:
            item_evento = Evento.objects.get(id=evento)
            return Combate.objects.filter(evento=item_evento)
