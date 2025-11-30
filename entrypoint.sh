#!/bin/sh

echo "Waiting for database..."
sleep 3

echo "Running migrations..."
python manage.py migrate --noinput

echo "Collecting static..."
python manage.py collectstatic --noinput

echo "Starting Gunicorn on port ${PORT}..."
exec gunicorn Nezapadni.wsgi:application --bind 0.0.0.0:${PORT}
