FROM python:3.7-alpine

ARG TAIGA_VERSION

WORKDIR /app

RUN apk add --no-cache postgresql-libs libxslt-dev libxml2-dev  libjpeg jpeg-dev \
    && apk add --no-cache --virtual build-deps git gcc python3-dev musl-dev libffi-dev postgresql-dev g++ libjpeg-turbo-dev  \
    && mkdir logs \
    && git clone --depth=1 -b $TAIGA_VERSION https://github.com/taigaio/taiga-back.git back \
    && cd back \
    && pip3 install --no-cache-dir -r requirements.txt \
    && pip3 install --no-cache-dir whitenoise django-jet \
    && rm -rf /root/.cache \
    && apk del build-deps \
    && rm /srv/taiga/back/settings/local.py.example

WORKDIR /app
# COPY config.py settings/local.py
RUN python manage.py collectstatic --noinput
