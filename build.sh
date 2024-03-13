#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input 
python manage.py makemigrations users
python manage.py makemigrations torneos
python manage.py makemigrations equipo_jugador
python manage.py makemigrations partidos_horario
python manage.py makemigrations tabla_posiciones
python manage.py migrate
python manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('adminangel', '', 'agl5702')"






