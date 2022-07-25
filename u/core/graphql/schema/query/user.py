from graphene import (
    Field, Argument, ID,
    NonNull, List, Float,
    ObjectType, Mutation,Boolean,String,
)

from django.contrib.auth import get_user_model

from ..type import (
    UserType,
    ProfileType,
)
from ..input import (
    UserInput,
)

from ...resolves import (
    get_user,
    get_all_users,
)

User = get_user_model()


class UserQuery:
    user = Field(UserType, id=Argument(ID, required=True))
    users = List(UserType, )
    profile = Field(ProfileType, id=Argument(ID, ))

    def resolve_user(self, info, **kwargs):
        id = kwargs.get("id")
        return get_user(id=id)

    def resolve_users(self,info):
        return get_all_users()


# Create mutations for user
class UserCreate(Mutation):
    class Arguments:
        input = UserInput(required=True)

    ok = Boolean()
    user = Field(UserType)
    error = String()
    @staticmethod
    def mutate(root, info, input=None):
        # print("sodfh[ohsf;lad")
        ok = False
        error = None
        user = None
        try:
            user_instance = User()

            user_instance.email = input.email
            user_instance.username = input.username
            user_instance.phone_number = input.phone_number
            user_instance.set_password(input.password)

            user_instance.save()

            ok = True
            user = user_instance

            return UserCreate(
                ok=ok,
                user=user_instance,
                error=error
            )

        except Exception as e:
            error = f"{e}"

            return UserCreate(
                ok=ok,
                user=user,
                error =error,

            )
