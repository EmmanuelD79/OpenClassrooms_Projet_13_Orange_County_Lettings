FROM python:3.11.0-alpine3.16

# This prevents Python from writing out pyc files
ENV PYTHONDONTWRITEBYTECODE 1

# This keeps Python from buffering stdin/stdout
ENV PYTHONUNBUFFERED 1

EXPOSE 8000

WORKDIR /app
COPY requirements.txt requirements.txt

RUN mkdir -p /assets \
    && mkdir -p /logs \
    && chmod u+x /app \
    && pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chmod u+x docker-entrypoint.sh

CMD ["app/docker-entrypoint.sh", "-n"]
