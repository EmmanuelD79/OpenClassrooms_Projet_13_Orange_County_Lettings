FROM python:3.11.0-alpine:3.16

# This prevents Python from writing out pyc files
ENV PYTHONDONTWRITEBYTECODE 1

# This keeps Python from buffering stdin/stdout
ENV PYTHONUNBUFFERED 1

EXPOSE 8000

WORKDIR /app
COPY requirements.txt /app/requirements.txt

RUN mkdir -p /app/assets \
    && mkdir -p /app/logs \
    && chmod 755 /app \
    && pip install --no-cache-dir -r /app/requirements.txt

COPY . /app

CMD ["/app/docker-entrypoint.sh", "-n"]
