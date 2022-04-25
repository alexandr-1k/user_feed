#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done
fi

python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py fill_db

exec "$@"