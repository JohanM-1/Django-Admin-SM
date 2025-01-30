#!/bin/sh

# Crear directorio de logs si no existe
mkdir -p /var/log/app

# Redirigir toda la salida a un archivo de log con timestamp
exec 1> >(while read line; do echo "$(date '+%Y-%m-%d %H:%M:%S') $line" | tee -a "/var/log/app/app.log"; done) 2>&1

python3 manage.py makemigrations
python3 manage.py migrate

# Print environment variables to verify
echo "Checking environment variables..."
echo "DJANGO_SUPERUSER_USERNAME: ${DJANGO_SUPERUSER_USERNAME}"
echo "DJANGO_SUPERUSER_EMAIL: ${DJANGO_SUPERUSER_EMAIL}"
echo "DJANGO_SUPERUSER_PASSWORD: ${DJANGO_SUPERUSER_PASSWORD}"

# Create superuser if it doesn't exist
echo "Creating superuser..."
DJANGO_SUPERUSER_PASSWORD=${DJANGO_SUPERUSER_PASSWORD} python3 manage.py createsuperuser \
    --username=${DJANGO_SUPERUSER_USERNAME} \
    --email=${DJANGO_SUPERUSER_EMAIL} \
    --noinput
    
python3 manage.py test
python3 manage.py runserver 0.0.0.0:8080 