from graphene_django import DjangoObjectType

from core.models import Profile


class ProfileType(DjangoObjectType):
    class Meta:
        model = Profile
        fields = "__all__"
