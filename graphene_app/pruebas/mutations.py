import graphene
from graphene import Mutation

from Espannol.pruebas.models import *


class NuevoLugar(graphene.Mutation):
    class Arguments:
        nombre = graphene.String(required=True)
        provincia = graphene.ID()

    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, nombre, provincia):
        try:
            item_provincia = Provincia.objects.get(id=provincia)
            Lugar.objects.create(nombre=nombre, provincia=item_provincia)
            return NuevoLugar(success=True, error=None)
        except Exception as e:
            return NuevoLugar(success=False, error=str(e))


class UpdateLugar(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        provincia = graphene.ID(required=True)
        nombre = graphene.String(required=True)

    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, nombre, id, provincia):
        try:
            item_provincia = Provincia.objects.get(id=provincia)
            lugar = Lugar.objects.get(id=id)
            lugar.nombre = nombre
            lugar.provincia = item_provincia
            lugar.save()
            return UpdateLugar(success=True, error=None)
        except Exception as e:
            return UpdateLugar(success=False, error=str(e))


class EliminarLugar(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, id):
        try:
            lugar = Lugar.objects.get(id=id)
            lugar.delete()
            return EliminarLugar(success=True, error=None)
        except Exception as e:
            return EliminarLugar(success=False, error=str(e))


class NuevaPrueba(Mutation):
    class Arguments:
        fecha = graphene.Date()
        deportista = graphene.ID()
        lugar = graphene.ID()
        etapa = graphene.String(required=True)

    success = graphene.Boolean()
    errors = graphene.String()

    def mutate(self, info, fecha, deportista, lugar, etapa):
        try:
            item_deportista = Deportista.objects.get(id=deportista)
            item_lugar = Lugar.objects.get(id=lugar)
            Prueba.objects.create(
                fecha=fecha,
                deportista=item_deportista,
                lugar=item_lugar,
                etapa=etapa
            )
            return NuevaPrueba(success=True, errors=None)
        except Exception as e:
            return NuevaPrueba(success=False, errors=str(e))


class UpdatePrueba(Mutation):
    class Arguments:
        fecha = graphene.Date()
        deportista = graphene.ID()
        lugar = graphene.ID()
        observaciones = graphene.String()
        valoracion = graphene.String()
        id = graphene.ID()
        etapa = graphene.String()

    success = graphene.Boolean()
    errors = graphene.String()

    def mutate(self, info, fecha, deportista, lugar, observaciones, valoracion, id, etapa):
        try:
            item_deportista = Deportista.objects.get(id=deportista)
            item_lugar = Lugar.objects.get(id=lugar)
            prueba = Prueba.objects.get(id=id)
            prueba.fecha = fecha
            prueba.deportista = item_deportista
            prueba.lugar = item_lugar
            prueba.valoracion = valoracion
            prueba.etapa = etapa
            prueba.observaciones = observaciones
            prueba.save()
            return UpdatePrueba(success=True, errors=None)
        except Exception as e:
            return UpdatePrueba(success=False, errors=str(e))


class NuevaRast(Mutation):
    class Arguments:
        prueba = graphene.ID()
        distancia = graphene.Decimal()
        tiempo_uno = graphene.Decimal()
        tiempo_dos = graphene.Decimal()
        tiempo_tres = graphene.Decimal()
        tiempo_quatro = graphene.Decimal()
        tiempo_cinco = graphene.Decimal()
        tiempo_seis = graphene.Decimal()

    success = graphene.Boolean()
    errors = graphene.String()

    def mutate(self, info, prueba, distancia, tiempo_uno, tiempo_dos, tiempo_tres, tiempo_quatro, tiempo_cinco,
               tiempo_seis):
        try:
            item_prueba = Prueba.objects.get(id=prueba)
            if Rast.objects.filter(prueba=item_prueba).exists():
                return NuevaRast(success=False, errors='Ya existen datos de esta prueba')
            rast = Rast.objects.create(
                prueba=item_prueba,
                distancia=distancia,
                tiempo_uno=tiempo_uno,
                tiempo_dos=tiempo_dos,
                tiempo_tres=tiempo_tres,
                tiempo_quatro=tiempo_quatro,
                tiempo_cinco=tiempo_cinco,
                tiempo_seis=tiempo_seis
            )
            return NuevaRast(success=True, errors=None)
        except Exception as e:
            return NuevaRast(success=False, errors=str(e))


class UpdateRast(Mutation):
    class Arguments:
        prueba = graphene.ID()
        distancia = graphene.Decimal()
        tiempo_uno = graphene.Decimal()
        tiempo_dos = graphene.Decimal()
        tiempo_tres = graphene.Decimal()
        tiempo_quatro = graphene.Decimal()
        tiempo_cinco = graphene.Decimal()
        tiempo_seis = graphene.Decimal()
        id = graphene.ID()

    success = graphene.Boolean()
    errors = graphene.String()

    def mutate(self, info, prueba, distancia, tiempo_uno, tiempo_dos, tiempo_tres, tiempo_quatro, tiempo_cinco,
               tiempo_seis, id):
        try:
            item_prueba = Prueba.objects.get(id=prueba)
            rast = Rast.objects.get(id=id)
            rast.prueba = item_prueba
            rast.distancia = distancia
            rast.tiempo_uno = tiempo_uno
            rast.tiempo_dos = tiempo_dos
            rast.tiempo_tres = tiempo_tres
            rast.tiempo_quatro = tiempo_quatro
            rast.tiempo_cinco = tiempo_cinco
            rast.tiempo_seis = tiempo_seis
            rast.save()
            return UpdateRast(success=True, errors=None)
        except Exception as e:
            return UpdateRast(success=False, errors=str(e))


class NuevaCarlson(Mutation):
    class Arguments:
        prueba = graphene.ID()
        frecuencia_cardiaca_antes = graphene.Int()
        frecuencia_cardiaca_despues = graphene.Int()
        frecuencia_cardiaca_min_uno = graphene.Int()
        frecuencia_cardiaca_min_tres = graphene.Int()
        frecuencia_cardiaca_min_cinco = graphene.Int()
        frecuencia_cardiaca_min_siete = graphene.Int()
        presion_sistolica_antes = graphene.Decimal()
        presion_diastolica_antes = graphene.Decimal()
        presion_sistolica_despues = graphene.Decimal()
        presion_diastolica_despues = graphene.Decimal()
        contactos_uno = graphene.Int()
        contactos_dos = graphene.Int()
        contactos_tres = graphene.Int()
        contactos_quatro = graphene.Int()
        contactos_cinco = graphene.Int()
        contactos_seis = graphene.Int()
        contactos_siete = graphene.Int()
        contactos_ocho = graphene.Int()
        contactos_nueve = graphene.Int()
        contactos_diez = graphene.Int()

    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, prueba, frecuencia_cardiaca_antes, frecuencia_cardiaca_despues, frecuencia_cardiaca_min_uno,
               frecuencia_cardiaca_min_tres, frecuencia_cardiaca_min_cinco, frecuencia_cardiaca_min_siete,
               presion_sistolica_antes, presion_diastolica_antes, presion_sistolica_despues, presion_diastolica_despues,
               contactos_uno, contactos_dos, contactos_tres, contactos_quatro, contactos_cinco, contactos_seis,
               contactos_siete,
               contactos_ocho, contactos_nueve, contactos_diez):
        try:
            item_prueba = Prueba.objects.get(id=prueba)
            if Carlson.objects.filter(prueba=item_prueba).exists():
                return NuevaCarlson(success=False, errors='Ya existen datos de esta prueba')
            Carlson.objects.create(
                prueba=item_prueba,
                frecuencia_cardiaca_antes=frecuencia_cardiaca_antes,
                frecuencia_cardiaca_despues=frecuencia_cardiaca_despues,
                frecuencia_cardiaca_min_uno=frecuencia_cardiaca_min_uno,
                frecuencia_cardiaca_min_tres=frecuencia_cardiaca_min_tres,
                frecuencia_cardiaca_min_cinco=frecuencia_cardiaca_min_cinco,
                frecuencia_cardiaca_min_siete=frecuencia_cardiaca_min_siete,
                presion_sistolica_antes=presion_sistolica_antes,
                presion_diastolica_antes=presion_diastolica_antes,
                presion_sistolica_despues=presion_sistolica_despues,
                presion_diastolica_despues=presion_diastolica_despues,
                contactos_uno=contactos_uno,
                contactos_dos=contactos_dos,
                contactos_tres=contactos_tres,
                contactos_quatro=contactos_quatro,
                contactos_cinco=contactos_cinco,
                contactos_seis=contactos_seis,
                contactos_siete=contactos_siete,
                contactos_ocho=contactos_ocho,
                contactos_nueve=contactos_nueve,
                contactos_diez=contactos_diez
            )
            return NuevaCarlson(success=True, error=None)

        except Exception as e:
            return NuevaCarlson(success=False, error=str(e))


class UpdateCarlson(Mutation):
    class Arguments:
        prueba = graphene.ID()
        frecuencia_cardiaca_antes = graphene.Int()
        frecuencia_cardiaca_despues = graphene.Int()
        frecuencia_cardiaca_min_uno = graphene.Int()
        frecuencia_cardiaca_min_tres = graphene.Int()
        frecuencia_cardiaca_min_cinco = graphene.Int()
        frecuencia_cardiaca_min_siete = graphene.Int()
        presion_sistolica_antes = graphene.Decimal()
        presion_diastolica_antes = graphene.Decimal()
        presion_sistolica_despues = graphene.Decimal()
        presion_diastolica_despues = graphene.Decimal()
        contactos_uno = graphene.Int()
        contactos_dos = graphene.Int()
        contactos_tres = graphene.Int()
        contactos_quatro = graphene.Int()
        contactos_cinco = graphene.Int()
        contactos_seis = graphene.Int()
        contactos_siete = graphene.Int()
        contactos_ocho = graphene.Int()
        contactos_nueve = graphene.Int()
        contactos_diez = graphene.Int()
        id = graphene.ID()

    success = graphene.Boolean()
    error = graphene.String()

    def mutate(self, info, prueba, frecuencia_cardiaca_antes, frecuencia_cardiaca_despues, frecuencia_cardiaca_min_uno,
               frecuencia_cardiaca_min_tres, frecuencia_cardiaca_min_cinco, frecuencia_cardiaca_min_siete,
               presion_sistolica_antes, presion_diastolica_antes, presion_sistolica_despues, presion_diastolica_despues,
               contactos_uno, contactos_dos, contactos_tres, contactos_quatro, contactos_cinco, contactos_seis,
               contactos_siete, id,
               contactos_ocho, contactos_nueve, contactos_diez):
        try:
            item_prueba = Prueba.objects.get(id=prueba)
            carlson = Carlson.objects.get(id=id)
            carlson.prueba = item_prueba
            carlson.frecuencia_cardiaca_antes = frecuencia_cardiaca_antes
            carlson.frecuencia_cardiaca_despues = frecuencia_cardiaca_despues
            carlson.frecuencia_cardiaca_min_uno = frecuencia_cardiaca_min_uno
            carlson.frecuencia_cardiaca_min_tres = frecuencia_cardiaca_min_tres
            carlson.frecuencia_cardiaca_min_cinco = frecuencia_cardiaca_min_cinco
            carlson.frecuencia_cardiaca_min_siete = frecuencia_cardiaca_min_siete
            carlson.presion_sistolica_antes = presion_sistolica_antes
            carlson.presion_diastolica_antes = presion_diastolica_antes
            carlson.presion_sistolica_despues = presion_sistolica_despues
            carlson.presion_diastolica_despues = presion_diastolica_despues
            carlson.contactos_uno = contactos_uno
            carlson.contactos_dos = contactos_dos
            carlson.contactos_tres = contactos_tres
            carlson.contactos_quatro = contactos_quatro
            carlson.contactos_cinco = contactos_cinco
            carlson.contactos_seis = contactos_seis
            carlson.contactos_siete = contactos_siete
            carlson.contactos_ocho = contactos_ocho
            carlson.contactos_nueve = contactos_nueve
            carlson.contactos_diez = contactos_diez
            carlson.save()

            return UpdateCarlson(success=True, error=None)

        except Exception as e:
            return UpdateCarlson(success=False, error=str(e))


class Mutation(graphene.ObjectType):
    nuevo_Lugar = NuevoLugar.Field()
    update_Lugar = UpdateLugar.Field()
    eliminar_Lugar = EliminarLugar.Field()
    nueva_Prueba = NuevaPrueba.Field()
    update_Prueba = UpdatePrueba.Field()
    nueva_Rast = NuevaRast.Field()
    update_Rast = UpdateRast.Field()
    nueva_Carlson = NuevaCarlson.Field()
    update_Carlson = UpdateCarlson.Field()
