import graphene
from django.db.models import Q
from graphene_django import DjangoObjectType

from Espannol.boxeo.models import *
from Espannol.nomencladores.models import Reglamento


class ReglamentoType(DjangoObjectType):
    class Meta:
        model = Reglamento
        fields = '__all__'


class CategoriaType(DjangoObjectType):
    class Meta:
        model = Categoria
        fields = '__all__'


class PugilType(DjangoObjectType):
    class Meta:
        model = Pugil
        fields = '__all__'


class DeportistaType(DjangoObjectType):
    class Meta:
        model = Deportista
        fields = '__all__'


class CombateType(DjangoObjectType):
    class Meta:
        model = Combate
        fields = '__all__'


class CodifResultadoType(DjangoObjectType):
    class Meta:
        model = CodifResultado
        fields = '__all__'


class ResultadoType(DjangoObjectType):
    class Meta:
        model = Resultado
        fields = '__all__'


class GolpeType(DjangoObjectType):
    class Meta:
        model = Golpe
        fields = '__all__'


class ContadorGolpesType(DjangoObjectType):
    class Meta:
        model = ContadorGolpes
        fields = '__all__'


class ConfigGolpeType(DjangoObjectType):
    class Meta:
        model = ConfigGolpe
        fields = '__all__'


class Query(graphene.ObjectType):
    reglamentos = graphene.List(ReglamentoType, name=graphene.String())
    categorias = graphene.List(CategoriaType, name=graphene.String())
    pugiles = graphene.List(PugilType, name=graphene.String())
    combates = graphene.List(CombateType, name=graphene.String())
    codifResult = graphene.List(CodifResultadoType, name=graphene.String())
    resultados = graphene.List(ResultadoType, name=graphene.String())
    golpes = graphene.List(GolpeType, name=graphene.String())
    contGolpes = graphene.List(ContadorGolpesType, combate=graphene.Int(), pugil=graphene.Int(),
                               round=graphene.Int())
    configGolpes = graphene.List(ConfigGolpeType, name=graphene.String(), usuario=graphene.Int())
    datosCombate = graphene.Field(CombateType, id=graphene.Int())
    resultadoCombate = graphene.Field(ResultadoType, combate=graphene.Int(), pugil=graphene.Int())
    cant_combates = graphene.Int()
    cant_victorias = graphene.Int()
    cant_cabeza = graphene.Int()
    cant_tronco = graphene.Int()
    efectivos = graphene.Int()
    fallados = graphene.Int()

    def resolve_resultadoCombate(self, info, combate, pugil):
        item_combate = Combate.objects.get(id=combate)
        item_pugil = Pugil.objects.get(id=pugil)
        if Resultado.objects.filter(Q(pugil=item_pugil) & Q(combate=item_combate)).exists():
            return Resultado.objects.get(Q(pugil=item_pugil) & Q(combate=item_combate))
        else:
            return None

    def resolve_datosCombate(self, info, id):
        combate = Combate.objects.get(id=id)
        return combate

    def resolve_reglamentos(self, info, name):
        if name == "":
            return Reglamento.objects.all()
        else:
            return Reglamento.objects.filter(tipo__icontains=name)

    def resolve_categorias(self, info, name):
        if name == "":
            return Categoria.objects.all()
        else:
            return Categoria.objects.filter(
                Q(categoria__icontains=name) | Q(peso_min__icontains=name) | Q(peso_max__icontains=name)

            )

    def resolve_pugiles(self, info, name):
        if name == "":
            return Pugil.objects.all()
        else:
            return Pugil.objects.filter(
                Q(deportista__nombre__icontains=name) | Q(deportista__edad__icontains=name) | Q(
                    deportista__peso__icontains=name) | Q(
                    categoria__categoria__icontains=name) | Q(deportista__pais__pais__icontains=name)
            )

    def resolve_combates(self, info, name):
        if name == "":
            return Combate.objects.all()
        else:
            return Combate.objects.filter(
                Q(fecha__icontains=name) | Q(esquinaA__deportista__nombre__icontains=name) | Q(
                    esquinaR__deportista__nombre__icontains=name) | Q(evento__nombre__icontains=name)

            )

    def resolve_codifResult(self, info, name):
        if name == "":
            return CodifResultado.objects.all()
        else:
            return CodifResultado.objects.filter(
                Q(resul__icontains=name) | Q(descripcion__icontains=name)

            )

    def resolve_resultados(self, info, name):
        if name == "":
            return Resultado.objects.all()
        else:
            return Resultado.objects.filter(
                Q(combate__fecha__icontains=name) | Q(pugil__pugil__icontains=name) | Q(
                    resultado__resultado__icontains=name)

            )

    def resolve_golpes(self, info, name):
        if name == "":
            return Golpe.objects.all()
        else:
            return Golpe.objects.filter(
                Q(golpe__icontains=name) | Q(siglas__icontains=name) | Q(efectivo__icontains=name)

            )

    def resolve_contGolpes(self, info, combate, pugil, round):
        comb = Combate.objects.get(id=combate)
        boxeador = Pugil.objects.get(id=pugil)
        golpes = ContadorGolpes.objects.filter(
            Q(combate=comb) &
            Q(esquina=boxeador)
        ).order_by('tiempo')
        if round == 0:
            return golpes
        else:
            return golpes.filter(numero_asalto=round)

    def resolve_configGolpes(self, info, name, usuario):
        if name == "":
            return ConfigGolpe.objects.filter(user=ExtendUser.objects.get(id=usuario))
        else:
            return ConfigGolpe.objects.filter(
                Q(tecla__icontains=name) | Q(golpe__golpe__icontains=name)
            )

    def resolve_cant_combates(self, info):
        return Combate.objects.all().count()

    def resolve_cant_victorias(self, info):
        return Resultado.objects.filter(resultado__resul__icontains="Victoria").count()

    def resolve_cant_cabeza(self, info):
        return ContadorGolpes.objects.filter(golpe__golpe__icontains='Cabeza').count()

    def resolve_cant_tronco(self, info):
        return ContadorGolpes.objects.filter(golpe__golpe__icontains='Tronco').count()

    def resolve_efectivos(self, info):
        return ContadorGolpes.objects.filter(golpe__efectivo=True).count()

    def resolve_fallados(self, info):
        return ContadorGolpes.objects.filter(golpe__efectivo=False).count()
