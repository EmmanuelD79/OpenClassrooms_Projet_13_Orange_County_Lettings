FROM python:3.11-slim

EXPOSE 8000

ARG SECRET_KEY
ARG SENTRY_DNS
ARG MODE

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PORT=8000
ENV SECRET_KEY=$SECRET_KEY
ENV SENTRY_DNS=$SENTRY_DNS
ENV MODE=$MODE

WORKDIR /app

# Install  requirements
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

# Collect static files in app
RUN python manage.py collectstatic --noinput

CMD gunicorn --bind 0.0.0.0:$PORT --timeout 5 --max-requests 600 --threads=10 --worker-class=sync oc_lettings_site.wsgi:application 