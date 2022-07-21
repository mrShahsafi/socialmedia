
# from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save

from .models import (
    Profile,
)

# from user.utils import generate_token

User = get_user_model()


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
