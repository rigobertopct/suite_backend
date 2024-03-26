import graphene


class CreateDeportistaSerializer(graphene.InputObjectType):
    nombre = graphene.String(required=True)
    edad = graphene.Int(required=True)
    pais = graphene.ID(required=True)
    ci = graphene.String(required=True)
    anno_deporte = graphene.Int(required=True)
    anno_nacional = graphene.Int(required=True)
    fecha_nacimiento = graphene.Date(required=True)


class UpdateDeportistaSerializer(graphene.InputObjectType):
    id = graphene.ID(required=True)
    nombre = graphene.String(required=True)
    edad = graphene.Int(required=True)
    pais = graphene.ID(required=True)
    ci = graphene.String(required=True)
    anno_deporte = graphene.Int(required=True)
    anno_nacional = graphene.Int(required=True)
    fecha_nacimiento = graphene.Date(required=True)


class DesactiveDeportistaSerializer(graphene.InputObjectType):
    id = graphene.ID(required=True)


class ActiveDeportistaSerializer(graphene.InputObjectType):
    id = graphene.ID(required=True)
