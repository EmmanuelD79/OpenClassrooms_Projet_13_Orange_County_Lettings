FROM python:3.11.0-alpine3.16

# This prevents Python from writing out pyc files
ENV PYTHONDONTWRITEBYTECODE 1

# This keeps Python from buffering stdin/stdout
ENV PYTHONUNBUFFERED 1

EXPOSE 8000

WORKDIR /app
COPY requirements.txt /app/requirements.txt

RUN mkdir -p /app/assets \
    && mkdir -p /app/logs \
    && chmod u+x /app \
    && pip install --no-cache-dir -r /app/requirements.txt

COPY . /app

RUN chmod u+x /app/docker-entrypoint.sh

CMD ["/app/docker-entrypoint.sh", "-n"]
