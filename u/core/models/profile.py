# django
from django.db.models import (
    CharField,
    BooleanField,
    OneToOneField,
    CASCADE,
    DateField,
    TextField,
    JSONField,
    URLField,
)
from django.utils.translation import gettext_lazy as _

# models
from .base import CommonBaseModel


# utils
from ..utils import get_default_extra_preferences


PROFILE_GENDER_CHOICES = [
    ("F", "Female"),
    ("M", "Male"),
    ("T", "Trans"),
    ("U", "UNKNOWN"),
]


class Profile(CommonBaseModel):
    user = OneToOneField(
        "User",
        on_delete=CASCADE,
    )
    bio = TextField(
        max_length=512,
        null=True,
        blank=True,
    )
    nickname = CharField(
        blank=True,
        null=True,
        max_length=150,
    )

    gender = CharField(
        max_length=6,
        choices=PROFILE_GENDER_CHOICES,
        null=True,
        blank=True,
        default="U",
    )
    is_block = BooleanField(
        default=False,
    )
    avatar = URLField(
        max_length=255,
        blank=True,
        null=True,
    )

    birth_date = DateField(
        null=True,
        blank=True,
    )

    extra_preferences = JSONField(
        default=get_default_extra_preferences,
        null=True,
        blank=True,
        help_text=_(
            "extra profile information's,such as user preferred communicating language with front-end and etc."
        ),
    )

    def __str__(self):
        return f"{self.id}, {self.user.username}"