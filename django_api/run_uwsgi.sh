#!/usr/bin/env bash

python manage.py migrate

python manage.py collectstatic --no-input

python manage.py compilemessages -l en -l ru

DJANGO_SUPERUSER_USERNAME="admin" DJANGO_SUPERUSER_PASSWORD="admin" DJANGO_SUPERUSER_PASSWORD="admin@example.com" \
python manage.py createsuperuser --noinput || true

set -e

chown www-data:www-data /var/log

uwsgi --strict --ini /etc/app/uwsgi.ini
