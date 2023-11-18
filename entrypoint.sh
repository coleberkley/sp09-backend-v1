#!/bin/sh

python3 manage.py migrate --no-input
python3 manage.py collectstatic

gunicorn sp09_skeleton.wsgi:application --bind 0.0.0.0:8000
