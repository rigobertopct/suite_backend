import graphene
from graphene import Mutation

from Espannol.Deportes.models import Deporte, Disciplina
from Espannol.boxeo.models import *
from Espannol.deportista.models import Deportista, DeportistaDisciplina
from Espannol.nomencladores.models import Pais, Evento, Reglamento
from Espannol.seguridad.models import Provincia
from .queries import CombateType


class NuevoCodifResultado(Mutation):
    class Arguments:
        resultado = graphene.String(required=True)
        descripcion = graphene.String(required=True)

    success = graphene.Boolean()
    errors = graphene.String()

    def mutate(self, info, resultado, descripcion):
        try:
            CodifResultado.objects.create(resul=resultado, descripcion=descripcion)
            return NuevoCodifResultado(success=True, errors=None)
        except Exception as e:
            return NuevoCodifResultado(success=False, errors=str(e))


class ActualizarCodifResultado(Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        resultado = graphene.String(required=True)
        descripcion = graphene.String(required=True)

    success = graphene.Boolean()
    errors = graphene.String()

    def mutate(self, info, resultado, id, descripcion):
        try:
            item = CodifResultado.objects.get(id=id)
            item.resul = resultado
            item.descripcion = descripcion
            item.save()
            return ActualizarCodifResultado(success=True, errors=None)
        except Exception as e:
            return ActualizarCodifResultado(success=False, errors=str(e))


class EliminarCodifResultado(Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    success = graphene.Boolean()
    errors = graphene.String()

    def mutate(self, info, id):
        try:
            item = CodifResultado.objects.get(id=id)
            item.delete()
            return EliminarCodifResultado(success=True, errors=None)
        except Exception as e:
            return EliminarCodifResultado(success=False, errors=str(e))


class NuevoReglamento(Mutation):
    class Arguments:
        tipo = graphene.String(required=True)
        cant_r = graphene.Int(required=True)
        duracion = graphene.Int(required=True)

    success = graphene.Boolean()
    errors = graphene.String()

    def mutate(self, info, tipo, cant_r, duracion):
        try:
            Reglamento.objects.create(tipo=tipo, cant_r=cant_r, duracion=duracion)
            return NuevoReglamento(success=True, errors=None)
        except Exception as e:
            return NuevoReglamento(success=False, errors=str(e))


class ActualizarReglamento(Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        tipo = graphene.String(required=True)
        cant_r = graphene.Int(required=True)
        duracion = graphene.Int(required=True)

    success = graphene.Boolean()
    errors = graphene.String()

    def mutate(self, info, tipo, cant_r, duracion, id):
        try:
            item = Reglamento.objects.get(id=id)
            item.tipo = tipo
            item.cant_r = cant_r
            item.duracion = duracion
            item.save()
            return ActualizarReglamento(success=True, errors=None)
        except Exception as e:
            return ActualizarReglamento(success=False, errors=str(e))


class EliminarReglamento(Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    success = graphene.Boolean()
    errors = graphene.String()

    def mutate(self, info, id):
        try:
            item = Reglamento.objects.get(id=id)
            item.delete()
            return EliminarReglamento(success=True, errors=None)
        except Exception as e:
            return EliminarReglamento(success=False, errors=str(e))


class NuevaCategoria(Mutation):
    class Arguments:
        categoria = graphene.String(required=True)
        peso_min = graphene.Decimal(required=False)
        peso_max = graphene.Decimal(required=False)

    success = graphene.Boolean()
    errors = graphene.String()

    def mutate(self, info, categoria, peso_min, peso_max):
        try:
            item_categoria = categoria
            pesoMin = peso_min
            pesoMax = peso_max
            Categoria.objects.create(categoria=item_categoria, peso_min=pesoMin, peso_max=pesoMax)
            return NuevaCategoria(success=True, errors=None)
        except Exception as e:
            return NuevaCategoria(success=False, errors=str(e))


class ActualizarCategoria(Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        categoria = graphene.String(required=False)
        peso_min = graphene.Decimal(required=False)
        peso_max = graphene.Decimal(required=False)

    success = graphene.Boolean()
    errors = graphene.String()

    def mutate(self, info, categoria, peso_min, peso_max, id):
        try:
            item = Categoria.objects.get(id=id)
            item.categoria = categoria
            item.peso_min = peso_min
            item.peso_max = peso_max
            item.save()
            return ActualizarCategoria(success=True, errors=None)
        except Exception as e:
            return ActualizarCategoria(success=False, errors=str(e))


class EliminarCategoria(Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    success = graphene.Boolean()
    errors = graphene.String()

    def mutate(self, info, id):
        try:
            item = Categoria.objects.get(id=id)
            item.delete()
            return EliminarCategoria(success=True, errors=None)
        except Exception as e:
            return EliminarCategoria(success=False, errors=str(e))


class NuevoPugil(Mutation):
    class Arguments:
        nombre = graphene.String(required=True)
        edad = graphene.Int(required=False)
        peso = graphene.Decimal(required=False)
        categoria = graphene.Int(required=True)
        pais = graphene.Int(required=True)
        ranking = graphene.String()
        provincia = graphene.ID()

    success = graphene.Boolean()
    errors = graphene.String()

    def mutate(self, info, nombre, edad, peso, categoria, pais, ranking, provincia):
        try:
            item_categoria = Categoria.objects.get(id=categoria)
            item_pais = Pais.objects.get(id=pais)
            item_provincia = Provincia.objects.get(id=provincia)

            if item_categoria.peso_min <= peso <= item_categoria.peso_max:
                pass
            else:
                return NuevoPugil(success=False, errors="Es púgil no pertenece a esa categoría")
            if Deporte.objects.filter(nombre__icontains='Boxeo').exists():
                item_deporte = Deporte.objects.filter(nombre__icontains='Boxeo').first()
            else:
                item_deporte = Deporte.objects.create(nombre='Boxeo', siglas='BX')
            if Disciplina.objects.filter(deporte=item_deporte).exists():
                if Disciplina.objects.filter(codigo__icontains=item_categoria.categoria).exists():
                    item_disciplina = Disciplina.objects.filter(codigo__icontains=item_categoria.categoria).first()
                else:
                    item_disciplina = Disciplina.objects.create(nombre="Masculino", deporte=item_deporte,
                                                                codigo=item_categoria.categoria)
            else:
                item_disciplina = Disciplina.objects.create(nombre="Masculino", deporte=item_deporte,
                                                            codigo=item_categoria.categoria)
            deportista = Deportista.objects.create(nombre=nombre, edad=edad, peso=peso, pais=item_pais,
                                                   deporte=item_deporte, provincia=item_provincia)
            DeportistaDisciplina.objects.create(disciplina=item_disciplina, deportista=deportista)
            Pugil.objects.create(deportista=deportista, categoria=item_categoria, ranking=ranking)
            return NuevoPugil(success=True, errors=None)
        except Exception as e:
            return NuevoPugil(success=False, errors=str(e))


class ActualizarPugil(Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        nombre = graphene.String(required=True)
        edad = graphene.Int(required=False)
        peso = graphene.Decimal(required=False)
        categoria = graphene.Int(required=True)
        pais = graphene.Int(required=True)
        ranking = graphene.String()

    success = graphene.Boolean()
    errors = graphene.String()

    def mutate(self, info, nombre, edad, peso, categoria, pais, id, ranking):
        try:
            pugil = Pugil.objects.get(id=id)
            item_categoria = Categoria.objects.get(id=categoria)
            item_pais = Pais.objects.get(id=pais)
            item = Deportista.objects.get(id=pugil.deportista.id)
            item.nombre = nombre
            item.edad = edad
            item.peso = peso
            item.pais = item_pais
            item.save()
            pugil.categoria = item_categoria
            pugil.ranking = ranking
            pugil.save()
            return ActualizarPugil(success=True, errors=None)
        except Exception as e:
            return ActualizarPugil(success=False, errors=str(e))


class EliminarPugil(Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    success = graphene.Boolean()
    errors = graphene.String()

    def mutate(self, info, id):
        try:
            item = Pugil.objects.get(id=id)
            item.delete()
            return EliminarPugil(success=True, errors=None)
        except Exception as e:
            return EliminarPugil(success=False, errors=str(e))


class NuevoCombate(Mutation):
    class Arguments:
        nombre = graphene.String()
        fecha = graphene.Date(required=True)
        esquinaA = graphene.Int(required=False)
        esquinaR = graphene.Int(required=False)
        evento = graphene.Int(required=True)

    success = graphene.Boolean()
    errors = graphene.String()
    combate = graphene.Field(CombateType)

    def mutate(self, info, fecha, esquinaA, esquinaR, evento, nombre):
        try:
            item_fecha = fecha
            item_esquinaA = Pugil.objects.get(id=esquinaA)
            item_esquinaR = Pugil.objects.get(id=esquinaR)
            item_evento = Evento.objects.get(id=evento)
            combate = Combate.objects.create(fecha=item_fecha, esquinaA=item_esquinaA, esquinaR=item_esquinaR,
                                             evento=item_evento, nombre=nombre)
            return NuevoCombate(success=True, errors=None, combate=combate)
        except Exception as e:
            return NuevoCombate(success=False, errors=str(e), combate=None)


class ActualizarCombate(Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        fecha = graphene.Date(required=False)
        esquinaA = graphene.Int(required=False)
        esquinaR = graphene.Decimal(required=False)
        evento = graphene.Int(required=True)

    success = graphene.Boolean()
    errors = graphene.String()

    def mutate(self, info, fecha, esquinaA, esquinaR, evento, id):
        try:
            item = Combate.objects.get(id=id)
            item_roja = Pugil.objects.get(id=esquinaR)
            item_azul = Pugil.objects.get(id=esquinaA)
            item_evento = Evento.objects.get(id=evento)
            item.fecha = fecha
            item.esquinaA = item_azul
            item.esquinaR = item_roja
            item.evento = item_evento
            item.save()
            return ActualizarCombate(success=True, errors=None)
        except Exception as e:
            return ActualizarCombate(success=False, errors=str(e))


class EliminarCombate(Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    success = graphene.Boolean()
    errors = graphene.String()

    def mutate(self, info, id):
        try:
            item = Combate.objects.get(id=id)
            item.delete()
            return EliminarCombate(success=True, errors=None)
        except Exception as e:
            return EliminarCombate(success=False, errors=str(e))


class NuevoResultado(Mutation):
    class Arguments:
        combate = graphene.Int(required=True)
        resultado = graphene.Int(required=False)
        pugil = graphene.Int(required=True)

    success = graphene.Boolean()
    errors = graphene.String()

    def mutate(self, info, combate, resultado, pugil):
        try:
            item_combate = Combate.objects.get(id=combate)
            item_resultado = CodifResultado.objects.get(id=resultado)
            item_pugil = Pugil.objects.get(id=pugil)
            if Resultado.objects.filter(combate=item_combate, pugil=item_pugil).exists():
                result = Resultado.objects.filter(combate=item_combate, pugil=item_pugil).first()
                result.resultado = item_resultado
                result.save()
            else:
                Resultado.objects.create(combate=item_combate, resultado=item_resultado, pugil=item_pugil)
            return NuevoResultado(success=True, errors=None)
        except Exception as e:
            return NuevoResultado(success=False, errors=str(e))


class ActualizarResultado(Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        combate = graphene.Int(required=False)
        resultado = graphene.Int(required=False)
        pugil = graphene.Int(required=False)

    success = graphene.Boolean()
    errors = graphene.String()

    def mutate(self, info, combate, resultado, pugil, id):
        try:
            item = Resultado.objects.get(id=id)
            item_pugil = Pugil.objects.get(id=pugil)
            item_combate = Combate.objects.get(id=combate)
            item_resultado = CodifResultado.objects.get(id=resultado)
            item.resultado = item_resultado
            item.combate = item_combate
            item.pugil = item_pugil
            item.save()
            return ActualizarResultado(success=True, errors=None)
        except Exception as e:
            return ActualizarResultado(success=False, errors=str(e))


class EliminarResultado(Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    success = graphene.Boolean()
    errors = graphene.String()

    def mutate(self, info, id):
        try:
            item = Resultado.objects.get(id=id)
            item.delete()
            return EliminarResultado(success=True, errors=None)
        except Exception as e:
            return EliminarResultado(success=False, errors=str(e))


class NuevoGolpe(Mutation):
    class Arguments:
        golpe = graphene.String(required=True)
        siglas = graphene.String(required=False)
        efectivo = graphene.Boolean(required=True)

    success = graphene.Boolean()
    errors = graphene.String()

    def mutate(self, info, golpe, siglas, efectivo):
        try:
            item_golpe = golpe
            item_siglas = siglas
            item_efectivo = efectivo
            Golpe.objects.create(golpe=item_golpe, siglas=item_siglas, efectivo=item_efectivo)
            return NuevoGolpe(success=True, errors=None)
        except Exception as e:
            return NuevoGolpe(success=False, errors=str(e))


class ActualizarGolpe(Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        siglas = graphene.String(required=False)
        golpe = graphene.String(required=False)
        efectivo = graphene.Boolean(required=False)

    success = graphene.Boolean()
    errors = graphene.String()

    def mutate(self, info, golpe, siglas, efectivo, id):
        try:
            item = Golpe.objects.get(id=id)
            item.golpe = golpe
            item.siglas = siglas
            item.efectivo = efectivo
            item.save()
            return ActualizarGolpe(success=True, errors=None)
        except Exception as e:
            return ActualizarGolpe(success=False, errors=str(e))


class EliminarGolpe(Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    success = graphene.Boolean()
    errors = graphene.String()

    def mutate(self, info, id):
        try:
            item = Golpe.objects.get(id=id)
            item.delete()
            return EliminarGolpe(success=True, errors=None)
        except Exception as e:
            return EliminarGolpe(success=False, errors=str(e))


class NuevoContador(Mutation):
    class Arguments:
        numero_asalto = graphene.Int(required=True)
        combate = graphene.Int(required=False)
        golpe = graphene.Int(required=True)
        esquina = graphene.Int(required=True)
        tiempo = graphene.String()

    success = graphene.Boolean()
    errors = graphene.String()

    def mutate(self, info, numero_asalto, combate, golpe, esquina, tiempo):
        try:
            item_numA = numero_asalto
            item_combate = Combate.objects.get(id=combate)
            item_golpe = Golpe.objects.get(id=golpe)
            item_esquina = Pugil.objects.get(id=esquina)
            ContadorGolpes.objects.create(tiempo=tiempo, golpe=item_golpe, numero_asalto=item_numA,
                                          combate=item_combate, esquina=item_esquina)
            return NuevoContador(success=True, errors=None)
        except Exception as e:
            return NuevoContador(success=False, errors=str(e))


class ActualizarContador(Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        numero_asalto = graphene.Int(required=False)
        combate = graphene.Int(required=False)
        golpe = graphene.Int(required=False)
        esquina = graphene.String(required=False)

    success = graphene.Boolean()
    errors = graphene.String()

    def mutate(self, info, numero_asalto, combate, golpe, esquina, id):
        try:
            item = ContadorGolpes.objects.get(id=id)
            item_golpe = Golpe.objects.get(id=id)
            item_combate = Combate.objects.get(id=id)
            item.numero_asalto = numero_asalto
            item.esquina = esquina
            item.combate = item_combate
            item.golpe = item_golpe
            item.save()
            return ActualizarContador(success=True, errors=None)
        except Exception as e:
            return ActualizarContador(success=False, errors=str(e))


class EliminarContador(Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    success = graphene.Boolean()
    errors = graphene.String()

    def mutate(self, info, id):
        try:
            item = ContadorGolpes.objects.get(id=id)
            item.delete()
            return EliminarContador(success=True, errors=None)
        except Exception as e:
            return EliminarContador(success=False, errors=str(e))


class NuevoConfiguracion(Mutation):
    class Arguments:
        tecla = graphene.String(required=True)
        golpe = graphene.Int(required=True)
        user = graphene.Int(required=True)

    success = graphene.Boolean()
    errors = graphene.String()

    def mutate(self, info, tecla, golpe, user):
        try:
            item_tecla = tecla
            item_golpe = Golpe.objects.get(id=golpe)
            item_user = ExtendUser.objects.get(id=user)
            ConfigGolpe.objects.create(golpe=item_golpe, tecla=item_tecla, user=item_user)
            return NuevoConfiguracion(success=True, errors=None)
        except Exception as e:
            return NuevoConfiguracion(success=False, errors=str(e))


class ActualizarConfiguracion(Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        tecla = graphene.String(required=False)
        golpe = graphene.Int(required=False)
        user = graphene.Int(required=False)

    success = graphene.Boolean()
    errors = graphene.String()

    def mutate(self, info, tecla, golpe, user, id):
        try:
            item = ConfigGolpe.objects.get(id=id)
            item_golpe = Golpe.objects.get(id=id)
            item_user = ExtendUser.objects.get(id=id)
            item.tecla = tecla
            item.golpe = item_golpe
            item.user = item_user
            item.save()
            return ActualizarConfiguracion(success=True, errors=None)
        except Exception as e:
            return ActualizarConfiguracion(success=False, errors=str(e))


class EliminarConfiguracion(Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    success = graphene.Boolean()
    errors = graphene.String()

    def mutate(self, info, id):
        try:
            item = ConfigGolpe.objects.get(id=id)
            item.delete()
            return EliminarConfiguracion(success=True, errors=None)
        except Exception as e:
            return EliminarConfiguracion(success=False, errors=str(e))


class Mutation(graphene.ObjectType):
    nuevoCodResultado = NuevoCodifResultado.Field()
    actualizarCodResultado = ActualizarCodifResultado.Field()
    eliminarCodResultado = EliminarCodifResultado.Field()
    nuevoReglamento = NuevoReglamento.Field()
    actualizarReglamento = ActualizarReglamento.Field()
    eliminarReglamento = EliminarReglamento.Field()
    nuevaCategoria = NuevaCategoria.Field()
    actualizarCategoria = ActualizarCategoria.Field()
    eliminarCategoria = EliminarCategoria.Field()
    nuevoPugil = NuevoPugil.Field()
    actualizarPugil = ActualizarPugil.Field()
    eliminarPugil = EliminarPugil.Field()
    nuevoCombate = NuevoCombate.Field()
    actualizarCombate = ActualizarCombate.Field()
    eliminarCombate = EliminarCombate.Field()
    nuevoResultado = NuevoResultado.Field()
    actualizarResultado = ActualizarResultado.Field()
    EliminarResultado = EliminarResultado.Field()
    nuevoGolpe = NuevoGolpe.Field()
    actualizarGolpe = ActualizarGolpe.Field()
    EliminarGolpe = EliminarGolpe.Field()
    nuevoContador = NuevoContador.Field()
    actualizarContador = ActualizarContador.Field()
    EliminarContador = EliminarContador.Field()
    nuevoConfiguracion = NuevoConfiguracion.Field()
    actualizarConfiguracion = ActualizarConfiguracion.Field()
    eliminarConfiguracion = EliminarConfiguracion.Field()
