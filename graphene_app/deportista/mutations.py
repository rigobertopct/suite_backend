import graphene
from graphene import Mutation

from Espannol.Deportes.models import Disciplina, Deporte
from Espannol.deportista.models import Deportista, DeportistaDisciplina
from Espannol.nomencladores.models import Pais
from Espannol.seguridad.models import Provincia


class NuevoDeportista(Mutation):
    class Arguments:
        nombre = graphene.String(required=True)
        edad = graphene.Int(required=False)
        peso = graphene.Decimal(required=False)
        estatura = graphene.Decimal(required=False)
        pais = graphene.ID(required=True)
        sexo = graphene.String(required=True)
        ci = graphene.String(required=True)
        anno_deporte = graphene.String(required=True)
        anno_nacional = graphene.String(required=True)
        fecha_nacimiento = graphene.Date(required=True)
        disciplina = graphene.List(graphene.ID)
        deporte = graphene.ID(required=True)
        provincia = graphene.ID(required=True)

    success = graphene.Boolean()
    errors = graphene.String()

    def mutate(self, info, nombre, edad, peso, pais, sexo, ci, anno_deporte, anno_nacional, fecha_nacimiento,
               disciplina, estatura, deporte, provincia):
        try:
            item_pais = Pais.objects.get(id=pais)
            item_deporte = Deporte.objects.get(id=deporte)
            item_provincia = Provincia.objects.get(id=provincia)
            deportista = Deportista.objects.create(
                nombre=nombre,
                edad=edad,
                estatura=estatura,
                peso=peso,
                pais=item_pais,
                sexo=sexo,
                ci=ci,
                anno_nacional=anno_nacional,
                anno_deporte=anno_deporte,
                fecha_nacimiento=fecha_nacimiento,
                deporte=item_deporte,
                provincia=item_provincia
            )
            for item in disciplina:
                DeportistaDisciplina.objects.create(deportista=deportista, disciplina_id=item)
            return NuevoDeportista(success=True, errors=None)
        except Exception as e:
            return NuevoDeportista(success=False, errors=str(e))


class UpdateDeportista(Mutation):
    class Arguments:
        nombre = graphene.String(required=True)
        edad = graphene.Int(required=False)
        peso = graphene.Decimal(required=False)
        estatura = graphene.Decimal(required=False)
        pais = graphene.ID(required=True)
        sexo = graphene.String(required=True)
        ci = graphene.String(required=True)
        anno_deporte = graphene.String(required=True)
        anno_nacional = graphene.String(required=True)
        fecha_nacimiento = graphene.Date(required=True)
        disciplina = graphene.List(graphene.ID)
        deporte = graphene.ID(required=True)
        id = graphene.ID(required=True)

    success = graphene.Boolean()
    errors = graphene.String()

    def mutate(self, info, nombre, edad, peso, pais, sexo, ci, anno_deporte, anno_nacional, fecha_nacimiento,
               disciplina, id, estatura, deporte):
        try:
            item_pais = Pais.objects.get(id=pais)
            item_deporte = Deporte.objects.get(id=deporte)
            deportista = Deportista.objects.get(id=id)
            deportista.nombre = nombre
            deportista.edad = edad
            deportista.estatura = estatura
            deportista.peso = peso
            deportista.deporte = item_deporte
            deportista.pais = item_pais
            deportista.sexo = sexo
            deportista.ci = ci
            deportista.anno_nacional = anno_nacional
            deportista.anno_deporte = anno_deporte
            deportista.fecha_nacimiento = fecha_nacimiento
            deportista.save()
            for item in DeportistaDisciplina.objects.filter(deportista=deportista):
                item.delete()
            for item in disciplina:
                DeportistaDisciplina.objects.create(deportista=deportista, disciplina_id=item)
            return UpdateDeportista(success=True, errors=None)
        except Exception as e:
            return UpdateDeportista(success=False, errors=str(e))


class ActiveDeportista(Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    success = graphene.Boolean()
    errors = graphene.String()

    def mutate(self, info, id):
        try:
            deportista = Deportista.objects.get(id=id)
            deportista.is_active = True
            deportista.save()
            return ActiveDeportista(success=True, errors=None)
        except Exception as e:
            return ActiveDeportista(success=False, errors=str(e))


class DesactiveDeportista(Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    success = graphene.Boolean()
    errors = graphene.String()

    def mutate(self, info, id):
        try:
            deportista = Deportista.objects.get(id=id)
            deportista.is_active = False
            deportista.save()
            return DesactiveDeportista(success=True, errors=None)
        except Exception as e:
            return DesactiveDeportista(success=False, errors=str(e))


class NuevoDeporte(graphene.Mutation):
    class Arguments:
        nombre = graphene.String(required=True)
        siglas = graphene.String(required=True)

    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, nombre, siglas):
        try:
            deporte = Deporte.objects.create(nombre=nombre, siglas=siglas)
            return NuevoDeporte(success=True, error=None)
        except Exception as e:
            return NuevoDeporte(success=False, error=str(e))


class UpdateDeporte(graphene.Mutation):
    class Arguments:
        nombre = graphene.String(required=True)
        siglas = graphene.String(required=True)
        id = graphene.ID(required=True)

    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, nombre, siglas, id):
        try:
            deporte = Deporte.objects.get(id=id)
            deporte.nombre = nombre
            deporte.siglas = siglas
            deporte.save()
            return UpdateDeporte(success=True, error=None)
        except Exception as e:
            return UpdateDeporte(success=False, error=str(e))


class EliminarDeporte(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, id):
        try:
            deporte = Deporte.objects.get(id=id)
            deporte.delete()
            return EliminarDeporte(success=True, error=None)
        except Exception as e:
            return EliminarDeporte(success=False, error=str(e))


class NuevaDisciplina(graphene.Mutation):
    class Arguments:
        nombre = graphene.String(required=True)
        deporte = graphene.ID(required=True)
        codigo = graphene.String(required=True)

    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, nombre, deporte, codigo):
        try:
            item_deporte = Deporte.objects.get(id=deporte)
            disciplina = Disciplina.objects.create(nombre=nombre, deporte=item_deporte, codigo=codigo)
            return NuevaDisciplina(success=True, error=None)
        except Exception as e:
            return NuevaDisciplina(success=False, error=str(e))


class UpdateDisciplina(graphene.Mutation):
    class Arguments:
        nombre = graphene.String(required=True)
        deporte = graphene.ID(required=True)
        codigo = graphene.String(required=True)
        id = graphene.ID(required=True)

    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, nombre, deporte, codigo, id):
        try:
            deporte_item = Deporte.objects.get(id=deporte)
            disciplina = Disciplina.objects.get(id=id)
            disciplina.nombre = nombre
            disciplina.codigo = codigo
            disciplina.deporte = deporte_item
            disciplina.save()
            return UpdateDisciplina(success=True, error=None)
        except Exception as e:
            return UpdateDisciplina(success=False, error=str(e))


class EliminarDisciplina(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, id):
        try:
            disciplina = Disciplina.objects.get(id=id)
            disciplina.delete()
            return EliminarDisciplina(success=True, error=None)
        except Exception as e:
            return EliminarDisciplina(success=False, error=str(e))


class Mutation(graphene.ObjectType):
    nuevo_Deportista = NuevoDeportista.Field()
    update_Deportista = UpdateDeportista.Field()
    active_Deportista = ActiveDeportista.Field()
    desactive_Deportista = DesactiveDeportista.Field()

    nuevo_deporte = NuevoDeporte.Field()
    update_deporte = UpdateDeporte.Field()
    eliminar_deporte = EliminarDeporte.Field()

    nueva_disciplina = NuevaDisciplina.Field()
    update_disciplina = UpdateDisciplina.Field()
    eliminar_disciplina = EliminarDisciplina.Field()
