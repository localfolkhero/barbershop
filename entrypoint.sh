#!/bin/sh

# Apply database migrations
echo "Applying database migrations..."
python manage.py migrate

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Start the Django application using Gunicorn
echo "Starting Django server with Gunicorn..."
# python manage.py runserver 0.0.0.0:8000
gunicorn barbershop.wsgi:application --bind 0.0.0.0:8000