#!/bin/sh
set -e

echo "Waiting for database..."
sleep 3

echo "Running migrations..."
python manage.py migrate --noinput

echo "Starting Gunicorn..."
# Если Railway НЕ передал PORT → используй 8000
PORT=${PORT:-8000}

gunicorn Nezapadni.wsgi:application \
    --bind 0.0.0.0:$PORT \
    --workers 3 \
    --log-level info
