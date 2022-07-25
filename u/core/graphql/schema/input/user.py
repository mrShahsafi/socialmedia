from graphene import (
    InputObjectType,
    String,

)


class UserInput(InputObjectType):
    email = String(required=True)
    username = String(required=True)
    phone_number = String(required=True)
    password = String(required=True)

    first_name = String()
    last_name = String()