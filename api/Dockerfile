FROM python:3.7.5-slim

EXPOSE 2064

WORKDIR /api

COPY . .

RUN pip install --upgrade pip 

RUN python -m pip install -r deps/requirements.txt

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y locales

RUN sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && \
    dpkg-reconfigure --frontend=noninteractive locales && \
    update-locale LANG=en_US.UTF-8

ENV LANG en_US.UTF-8 

ENV PYTHONPATH /api/modules

CMD gunicorn -c gunicorn.conf.py wsgi:app 
