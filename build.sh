#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input 
python manage.py migrate
python manage.py createsuperuser --noinput --username adminwinadmin --email admin@example.com
python manage.py makemigrations
python manage.py runserver
