#!/bin/bash

# apply database migrations
python3.11 manage.py migrate --noinput

# collect static files
python3.11 manage.py collectstatic --noinput

python3.11 manage.py runserver 0.0.0.0:8000

# Start Gunicorn processes
#echo Starting Gunicorn.

#exec gunicorn app.wsgi:application \
#    --name app \
#    --bind 0.0.0.0:80 \
#    --workers 3 \
#    --log-level=info \
#    --log-file=/src/logs/gunicorn.log \
#    --access-logfile=/src/logs/access.log \
#    "$@"