#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input 
python manage.py migrate

# Generar una contraseña aleatoria
password=$(openssl rand -base64 12)

# Crear superusuario y establecer la contraseña generada
echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin2', 'admin@example.com', '$password')" | python manage.py shell





