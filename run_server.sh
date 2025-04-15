#!/usr/bin/env bash

python3 manage.py migrate
python3 manage.py collectstatic --no-default-ignore --noinput
gunicorn --bind=0.0.0.0:8000 --workers=${WEB_WORKERS:-4} --timeout=120 --reload --log-file=/usr/src/app/logs/django_server.log app.wsgi:application