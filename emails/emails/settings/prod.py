
from .base import *

DEBUG = False

ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": os.getenv("DB_NAME", default="db"),
        "USER": os.getenv("DB_USER", default="root"),
        "PASSWORD": os.getenv("DB_PASS", default="root-password"),
        "HOST": "postgres",
        "PORT": "5432",
    }
}


