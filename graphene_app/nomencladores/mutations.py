import graphene
from graphene import Mutation

from Espannol.boxeo.models import Golpe, ConfigGolpe
from Espannol.nomencladores.models import Pais, TipoEvento, Evento, Reglamento
from Espannol.seguridad.models import ExtendUser


class NuevoPais(Mutation):
    class Arguments:
        pais = graphene.String(required=True)
        siglas = graphene.String(required=True)

    success = graphene.Boolean()
    errors = graphene.String()

    def mutate(self, info, pais, siglas):
        try:
            Pais.objects.create(pais=pais, siglas=siglas)
            return NuevoPais(success=True, errors=None)
        except Exception as e:
            return NuevoPais(success=False, errors=str(e))


class ActualizarPais(Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        pais = graphene.String(required=True)
        siglas = graphene.String(required=True)

    success = graphene.Boolean()
    errors = graphene.String()

    def mutate(self, info, pais, siglas, id):
        try:
            paiss = Pais.objects.get(id=id)
            paiss.pais = pais
            paiss.siglas = siglas
            paiss.save()
            return ActualizarPais(success=True, errors=None)
        except Exception as e:
            return ActualizarPais(success=False, errors=str(e))


class EliminarPais(Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    success = graphene.Boolean()
    errors = graphene.String()

    def mutate(self, info, id):
        try:
            paiss = Pais.objects.get(id=id)
            paiss.delete()
            return EliminarPais(success=True, errors=None)
        except Exception as e:
            return EliminarPais(success=False, errors=str(e))


class NuevoTipoEvento(Mutation):
    class Arguments:
        nombre = graphene.String(required=True)

    success = graphene.Boolean()
    errors = graphene.String()

    def mutate(self, info, nombre):
        try:
            TipoEvento.objects.create(tipo=nombre)
            return NuevoTipoEvento(success=True, errors=None)
        except Exception as e:
            return NuevoTipoEvento(success=False, errors=str(e))


class ActualizarTipoEvento(Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        nombre = graphene.String(required=True)

    success = graphene.Boolean()
    errors = graphene.String()

    def mutate(self, info, nombre, id):
        try:
            item = TipoEvento.objects.get(id=id)
            item.tipo = nombre
            item.save()
            return ActualizarTipoEvento(success=True, errors=None)
        except Exception as e:
            return ActualizarTipoEvento(success=False, errors=str(e))


class EliminarTipoEvento(Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    success = graphene.Boolean()
    errors = graphene.String()

    def mutate(self, info, id):
        try:
            item = TipoEvento.objects.get(id=id)
            item.delete()
            return EliminarTipoEvento(success=True, errors=None)
        except Exception as e:
            return EliminarTipoEvento(success=False, errors=str(e))


class NuevoEvento(Mutation):
    class Arguments:
        nombre = graphene.String(required=True)
        pais = graphene.Int(required=True)
        reglamento = graphene.Int(required=True)
        tipoevento = graphene.Int(required=True)
        anno = graphene.Int(required=True)

    success = graphene.Boolean()
    errors = graphene.String()

    def mutate(self, info, nombre, pais, reglamento, tipoevento, anno):
        try:
            item_pais = Pais.objects.get(id=pais)
            item_reglamento = Reglamento.objects.get(id=reglamento)
            item_tipoevento = TipoEvento.objects.get(id=tipoevento)
            Evento.objects.create(nombre=nombre, pais=item_pais, reglamento=item_reglamento,
                                  tipoevento=item_tipoevento, anno=anno)
            return NuevoEvento(success=True, errors=None)
        except Exception as e:
            return NuevoEvento(success=False, errors=str(e))


class ActualizarEvento(Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        nombre = graphene.String(required=True)
        pais = graphene.Int(required=True)
        reglamento = graphene.Int(required=True)
        tipoevento = graphene.Int(required=True)
        anno = graphene.Int(required=True)

    success = graphene.Boolean()
    errors = graphene.String()

    def mutate(self, info, nombre, pais, reglamento, tipoevento, id, anno):
        try:
            item = Evento.objects.get(id=id)
            item_pais = Pais.objects.get(id=pais)
            item_reglamento = Reglamento.objects.get(id=reglamento)
            item_tipoevento = TipoEvento.objects.get(id=tipoevento)
            item.nombre = nombre
            item.pais = item_pais
            item.anno = anno
            item.reglamento = item_reglamento
            item.tipoevento = item_tipoevento
            item.save()
            return ActualizarEvento(success=True, errors=None)
        except Exception as e:
            return ActualizarEvento(success=False, errors=str(e))


class EliminarEvento(Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    success = graphene.Boolean()
    errors = graphene.String()

    def mutate(self, info, id):
        try:
            item = Evento.objects.get(id=id)
            item.delete()
            return EliminarEvento(success=True, errors=None)
        except Exception as e:
            return EliminarEvento(success=False, errors=str(e))


class CrearUsuario(Mutation):
    class Arguments:
        nombre = graphene.String()
        apellidos = graphene.String()
        usuario = graphene.String()
        email = graphene.String()
        password = graphene.String()

    error = graphene.String()
    success = graphene.Boolean()

    def mutate(self, info, nombre, apellidos, usuario, email, password):
        try:
            usuario = ExtendUser.objects.create(email=email, first_name=nombre, last_name=apellidos, username=usuario)
            usuario.set_password(password)
            usuario.save()
            return CrearUsuario(error=None, success=True)
        except Exception as e:
            return CrearUsuario(error=str(e), success=False)


class NuevaTecla(Mutation):
    class Arguments:
        tecla = graphene.String()
        golpe = graphene.Int()
        usuario = graphene.Int()

    error = graphene.String()
    success = graphene.Boolean()

    def mutate(self, info, tecla, usuario, golpe):
        try:
            item_golpe = Golpe.objects.get(id=golpe)
            item_usuario = ExtendUser.objects.get(id=usuario)
            teclas = ConfigGolpe.objects.filter(user=item_usuario)
            if teclas.filter(tecla=tecla).exists():
                return NuevaTecla(error="Ya tienes configurado esa tecla", success=False)
            if teclas.filter(golpe=item_golpe).exists():
                return NuevaTecla(error="Ya tienes configurado ese golpe", success=False)
            ConfigGolpe.objects.create(golpe=item_golpe, user=item_usuario, tecla=tecla)
            return NuevaTecla(error=None, success=True)
        except Exception as e:
            return NuevaTecla(error=str(e), success=False)


class ActualizarTecla(Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        tecla = graphene.String()
        golpe = graphene.Int()
        usuario = graphene.Int()

    error = graphene.String()
    success = graphene.Boolean()

    def mutate(self, info, tecla, usuario, golpe, id):
        try:
            item_Tecla = ConfigGolpe.objects.get(id=id)
            item_golpe = Golpe.objects.get(id=golpe)
            item_usuario = ExtendUser.objects.get(id=usuario)
            teclas = ConfigGolpe.objects.filter(user=item_usuario)
            if teclas.filter(tecla=tecla).exclude(id=id).exists():
                return NuevaTecla(error="Ya tienes configurado esa tecla", success=False)
            if teclas.filter(golpe=item_golpe).exclude(id=id).exists():
                return NuevaTecla(error="Ya tienes configurado ese golpe", success=False)
            item_Tecla.golpe = item_golpe
            item_Tecla.user = item_usuario
            item_Tecla.tecla = tecla
            item_Tecla.save()
            return ActualizarTecla(error=None, success=True)
        except Exception as e:
            return ActualizarTecla(error=str(e), success=False)


class EliminarTecla(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    error = graphene.String()
    success = graphene.Boolean()

    def mutate(self, info, id):
        try:
            tecla = ConfigGolpe.objects.get(id=id)
            tecla.delete()
            return EliminarTecla(error=None, success=True)
        except Exception as e:
            return EliminarTecla(error=str(e), success=False)


class Mutation(graphene.ObjectType):
    nuevoPais = NuevoPais.Field()
    actualizarPais = ActualizarPais.Field()
    eliminarPais = EliminarPais.Field()
    nuevoTipoEvento = NuevoTipoEvento.Field()
    actualizarTipoEvento = ActualizarTipoEvento.Field()
    eliminarTipoEvento = EliminarTipoEvento.Field()
    nuevoEvento = NuevoEvento.Field()
    actualizarEvento = ActualizarEvento.Field()
    eliminarEvento = EliminarEvento.Field()
    crearUsuario = CrearUsuario.Field()
    nuevaTecla = NuevaTecla.Field()
    actualizarTecla = ActualizarTecla.Field()
    eliminarTecla = EliminarTecla.Field()
