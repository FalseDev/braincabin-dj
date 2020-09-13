from pathlib import Path
import os

try:
    DATABASE_ENGINE = os.environ['DATABASE_ENGINE']
except KeyError:
    DATABASE_ENGINE = 'django.db.backends.sqlite3'

try:
    DATABASE_NAME = os.environ['DATABASE_NAME']
except KeyError:
    DATABASE_NAME = os.path.join(Path(__file__).resolve().parent.parent, 'sqlite3')

try:
    DATABASE_USER = os.environ['DATABASE_USER']
except KeyError:
    DATABASE_USER = ''

try:
    DATABASE_PASSWORD = os.environ['DATABASE_PASSWORD']
except KeyError:
    DATABASE_PASSWORD = ''

try:
    DATABASE_HOST = os.environ['DATABASE_HOST']
except KeyError:
    DATABASE_HOST = ''

try:
    DATABASE_PORT = os.environ['DATABASE_PORT']
except KeyError:
    DATABASE_PORT = ''

