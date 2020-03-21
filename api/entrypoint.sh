#!/bin/bash

if [ -d "/build" ]
then
    cp /build/Pipfile.lock /build/Pipfile /api \
    && rm -rf /build \
    && python run.py
else
    python run.py
fi