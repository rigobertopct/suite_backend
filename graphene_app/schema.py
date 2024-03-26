import graphene
from graphql_auth import mutations
from graphql_auth.schema import UserQuery

from .boxeo.mutations import Mutation as BoxeoMutation
from .boxeo.queries import Query as BoxeoQuery
from .deportista.mutations import Mutation as DeportistaMutation
from .deportista.queries import Query as DeportistaQuery
from .nomencladores.mutations import Mutation as NomencladoresMutation
from .nomencladores.queries import Query as NomencladoresQuery
from .pruebas.mutations import Mutation as PruebasMutation
from .pruebas.queries import Query as PruebasQuery
from .seguridad.mutations import Mutation as SeguridadMutation
from .seguridad.queries import Query as SeguridadQuery


class AuthMutation(graphene.ObjectType):
    verify_account = mutations.VerifyAccount.Field()
    resend_activation_email = mutations.ResendActivationEmail.Field()
    send_password_reset_email = mutations.SendPasswordResetEmail.Field()
    password_reset = mutations.PasswordReset.Field()
    password_change = mutations.PasswordChange.Field()
    archive_account = mutations.ArchiveAccount.Field()
    delete_account = mutations.DeleteAccount.Field()
    update_account = mutations.UpdateAccount.Field()
    token_auth = mutations.ObtainJSONWebToken.Field()
    verify_token = mutations.VerifyToken.Field()
    refresh_token = mutations.RefreshToken.Field()
    revoke_token = mutations.RevokeToken.Field()


class Query(UserQuery, BoxeoQuery, SeguridadQuery, NomencladoresQuery, DeportistaQuery, PruebasQuery,
            graphene.ObjectType):
    pass


class Mutation(AuthMutation, BoxeoMutation, SeguridadMutation, NomencladoresMutation, DeportistaMutation,
               PruebasMutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
