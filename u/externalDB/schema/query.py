# graphql_api/schema/query.py

from graphene import (
    ObjectType,
    String,
)
from core.graphql.schema.query import UserQuery


class Query(ObjectType, UserQuery):
    status = String()

    def resolve_hello(self, info):
        return "ok"
