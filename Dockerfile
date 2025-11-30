# ---- Base image ----
FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

# ---- Run migrations ----
RUN python manage.py migrate --noinput

# ---- Collect static files ----
RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD gunicorn Nezapadni.wsgi:application --bind 0.0.0.0:$PORT
