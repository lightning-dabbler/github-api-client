#!/usr/bin/env bash

if [ -d "/build" ]
then
    cp /build/Pipfile.lock /build/Pipfile /api \
    && rm -rf /build \
    && gunicorn -c gunicorn.conf.py wsgi:app
else
    gunicorn -c gunicorn.conf.py wsgi:app
fi