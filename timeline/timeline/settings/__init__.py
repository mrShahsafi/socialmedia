
from os import getenv

env = getenv("DJANGO_ENV", default="development")

if env == "production":
    print("You Are in the Production Mode.")
    from .prod import *

elif env == "development":
    print("Warning! You Are in the Development Mode.Do Not use in any server.")
    
    from .dev import *
