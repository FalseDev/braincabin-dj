from os import environ
from django.core.exceptions import ImproperlyConfigured

# Mail configuration
try:
    EMAIL_BACKEND = environ['EMAIL_BACKEND']
    EMAIL_HOST = environ['EMAIL_HOST']
    EMAIL_PORT = int(environ['EMAIL_PORT'])
    EMAIL_USE_TLS = environ['EMAIL_USE_TLS'] == 'True'
    EMAIL_HOST_USER = environ['EMAIL_HOST_USER']
    EMAIL_HOST_PASSWORD = environ['EMAIL_HOST_PASSWORD']

    EMAIL_SERVER = EMAIL_HOST
    EMAIL_FROM_ADDRESS = EMAIL_HOST_USER
    EMAIL_ADDRESS = EMAIL_HOST_USER
    EMAIL_PASSWORD = EMAIL_HOST_PASSWORD

except (KeyError):
    pass
except:
    raise ImproperlyConfigured
