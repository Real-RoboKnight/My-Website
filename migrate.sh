#!/bin/sh
set -e

docker compose build

docker compose run --rm \
  -v "$(pwd)/home_page/django/personal_site/migrations:/app/members/migrations" \
  home_page \
  sh -c "python manage.py makemigrations $@ && python manage.py migrate"
