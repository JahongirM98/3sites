# docker/app.Dockerfile
FROM python:3.12-slim

# Путь сервиса (папка одного из проектов) прокидываем аргументом сборки
ARG SERVICE_PATH

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential libpq-dev && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# ОДИН общий requirements.txt из корня репозитория
COPY requirements-dev.txt /tmp/requirements-dev.txt
RUN pip install --no-cache-dir -r /tmp/requirements-dev.txt

# Копируем код ТОЛЬКО выбранного сервиса
COPY ${SERVICE_PATH}/ /app/

# В dev переопределим командой runserver в compose
CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3"]
