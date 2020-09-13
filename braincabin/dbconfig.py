from pathlib import Path
from os.path import join

try:
    DATABASE_ENGINE = os.environ['DATABASE_ENGINE']
except:
    DATABASE_ENGINE = 'django.db.backends.sqlite3'

try:
    DATABASE_NAME = os.environ['DATABASE_NAME']
except:
    DATABASE_NAME = join(Path(__file__).resolve().parent.parent, 'sqlite3')

try:
    DATABASE_USER = os.environ['DATABASE_USER']
except:
    DATABASE_USER = ''

try:
    DATABASE_PASSWORD = os.environ['DATABASE_PASSWORD']
except:
    DATABASE_PASSWORD = ''

try:
    DATABASE_HOST = os.environ['DATABASE_HOST']
except:
    DATABASE_HOST = ''

try:
    DATABASE_PORT = os.environ['DATABASE_PORT']
except:
    DATABASE_PORT = ''

