#!/bin/sh

# Run migrations
python manage.py migrate

# Collect static files (uncomment if needed)
# python manage.py collectstatic --noinput

# Start Gunicorn
exec gunicorn -b 0.0.0.0:8000 the_void.wsgi:application --log-level=debug
