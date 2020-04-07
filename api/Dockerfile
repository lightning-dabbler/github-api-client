FROM python:3.7-slim

EXPOSE 2064

WORKDIR /build

COPY Pipfile /build/


RUN pip install --upgrade pip \
    && pip install pipenv \
    && pipenv lock --clear

RUN pipenv install --system --deploy --ignore-pipfile --skip-lock --verbose


RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y locales

RUN sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && \
    dpkg-reconfigure --frontend=noninteractive locales && \
    update-locale LANG=en_US.UTF-8

ENV LANG en_US.UTF-8 

ENV PYTHONPATH /api/modules

WORKDIR /api

COPY . /api

CMD gunicorn -c gunicorn.conf.py wsgi:app