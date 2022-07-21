from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):

    def create_user(
            self,
            email,
            password,
            username,
            first_name=None,
            last_name=None,
            phone_number=None,
            is_active=False,
            is_staff=False,
    ):

        user = self.model(
            email=self.normalize_email(email.lower()),
            username=username,
            is_active=is_active,
            first_name=first_name,
            last_name=last_name,
            is_staff=is_staff,
            phone_number=phone_number,
        )

        if password is not None:
            user.set_password(password)
        else:
            user.set_unusable_password()

        user.save(using=self._db)

        return user

    def create_superuser(self, email=None, password=None, username=None):
        user = self.create_user(
            email=email,
            password=password,
            username=username,
        )
        user.is_superuser, user.is_staff, user.is_active = True, True, True
        user.save(using=self._db)
        return user

    def all_actives(self):
        qs = self.filter(
            is_active=True,
        )
        return qs

    def all_not_blocked(self):
        qs = self.filter(
            profile__is_block=True,
        )
        return qs
