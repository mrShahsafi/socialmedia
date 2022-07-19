from uuid import uuid4

from django.db.models import (
    UUIDField,
    EmailField,
    CharField,
    BooleanField,
    PositiveIntegerField,
)

from django.contrib.auth.models import (
    PermissionsMixin,
    AbstractBaseUser,
)
from django.utils.translation import gettext_lazy as _

from .base import CommonBaseModel as Model
from ..managers import UserManager


class User(Model, AbstractBaseUser, PermissionsMixin):
    id = UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False,
    )
    email = EmailField(
        _("email address"),
        unique=True,
    )

    username = CharField(
        _("username"),
        max_length=50,
        unique=True,
    )

    phone_number = PositiveIntegerField(
        _("email address"),
        unique=True,
        null=True,
        blank=True,
    )
    first_name = CharField(
        _("first name"),
        max_length=150,
        null=True,
        blank=True,
    )
    last_name = CharField(
        _("last name"),
        max_length=150,
        null=True,
        blank=True,
    )

    is_staff = BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )

    USERNAME_FIELD = "username"
    EMAIL_FIELD = "email"

    objects = UserManager()

    @property
    def get_fullname(self):

        fullname = f"{self.first_name} {self.last_name}"

        return fullname

    def __str__(self):
        name = f"{self.username}:{self.email}"

        return name
