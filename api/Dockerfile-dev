FROM python:3.7-slim

EXPOSE 2064

WORKDIR /build

COPY Pipfile /build/


RUN pip install --upgrade pip \
    && pip install pipenv \
    && pipenv lock --clear

RUN pipenv install --system --deploy --ignore-pipfile --skip-lock --verbose

WORKDIR /api