from graphene_django import DjangoObjectType

from django.contrib.auth import get_user_model

User = get_user_model()


class UserType(DjangoObjectType):
    # user_profile = List(NonNull(ProfileType),)
    #
    # def resolve_user_profile(self, info):
    #     return self.profile

    class Meta:
        model = User
        fields = "__all__"
