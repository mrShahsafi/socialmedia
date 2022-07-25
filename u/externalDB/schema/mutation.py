from graphene import ObjectType
from core.graphql.schema.query import UserCreate


class Mutation(ObjectType):
    create_user = UserCreate.Field()
