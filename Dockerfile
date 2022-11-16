FROM python:3.9

EXPOSE 8000

# Set environment variables
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV DEBUG=0
ENV PORT 8000

WORKDIR /app

# Install  requirements
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

# Collect static files in app
RUN python manage.py collectstatic --noinput --clear

CMD gunicorn oc_lettings_site.wsgi:application --bind 0.0.0.0:$PORT