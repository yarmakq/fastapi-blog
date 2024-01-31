FROM python:3.12.1-slim-bullseye

ARG FASTAPI_ENV \
  # Needed for fixing permissions of files created by Docker:
  UID=1000 \
  GID=1000

ENV FASTAPI_ENV=${FASTAPI_ENV} \
  # python:
  PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1

WORKDIR /app

COPY pyproject.toml poetry.lock ./

RUN python3 -m pip install --no-cache-dir poetry==1.7.1 \
    && poetry config --local virtualenvs.create false \
    && poetry install

COPY . /app
