#!/bin/bash

echo "Waiting for database..."
sleep 3

echo "Running migrations..."
python manage.py migrate --noinput

echo "Starting Gunicorn..."
gunicorn Nezapadni.wsgi:application --bind 0.0.0.0:${PORT}
