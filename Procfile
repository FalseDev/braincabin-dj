release: python manage.py makemigrations && python manage.py migrate
web: gunicorn braincabin.wsgi --log-file -
