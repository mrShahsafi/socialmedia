
from .base import *

# import socket  # only if you haven't already imported this

DEBUG = True

ALLOWED_HOSTS = [
    "localhost",
    "127.0.0.1",
]

try:
    from .local import *
except Exception:
    pass

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR / "db.sqlite3",
#     }
# }
#
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": os.getenv("DB_NAME", default="yuruma"),
        "USER": os.getenv("DB_USER", default="yurumauser"),
        "PASSWORD": os.getenv("DB_PASS", default="2187481"),
        "PORT": "5432",
    }
}

INSTALLED_APPS += [
    "debug_toolbar",
    #    'django_extensions'
]

MIDDLEWARE += [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

"""
    These commented config  will use         when you are running the project on Docker. 
"""
# hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
# INTERNAL_IPS = [ip[:-1] + "1" for ip in ips] + ["127.0.0.1", "10.0.2.2"]

INTERNAL_IPS = ["127.0.0.1", "10.0.2.2"]
