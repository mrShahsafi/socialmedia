from django.contrib.auth import get_user_model

User = get_user_model()


def get_all_users():
    try:
        qs = User.objects.all_actives()
        return qs

    except Exception as e:
        return e


def get_user(id):
    try:
        qs = User.objects.get(id=id)
        return qs

    except Exception as e:
        return e
