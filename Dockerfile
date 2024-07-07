FROM python:3.10

RUN pip install poetry

RUN pip install pip setuptools
RUN pip install celery redis

WORKDIR /app

COPY pyproject.toml poetry.lock ./

RUN poetry install --no-dev