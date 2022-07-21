# graphql_api/schema/query.py

from graphene import (
    ObjectType,
    String,
)
# from wallet.graphql.schema.query import WalletQuery


class Query(ObjectType,):
    hello = String()

    def resolve_hello(self, info):
        return "world"