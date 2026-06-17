#!/bin/sh
set -e

yes yes | python manage.py collectstatic 

gunicorn --config /app/gunicorn.conf.py