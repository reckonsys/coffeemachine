FROM alpine:latest

ARG VERSION=5.0.2


WORKDIR /srv/taiga

RUN apk --no-cache add python3 gettext postgresql-dev libxslt-dev libxml2-dev libjpeg-turbo-dev zeromq-dev libffi-dev \
	&& apk add --no-cache --virtual .build-dependencies git g++ musl-dev linux-headers python3-dev zlib-dev libjpeg-turbo-dev freetype-dev \
	&& mkdir logs \
	&& git clone --depth=1 -b $VERSION https://github.com/taigaio/taiga-back.git back \
    && cd back \
	&& pip3 install --no-cache-dir -r requirements.txt \
	&& rm -rf /root/.cache \
	&& apk del .build-dependencies \
	&& rm /srv/taiga/back/settings/local.py.example

WORKDIR /srv/taiga/back

COPY config.py settings/local.py

RUN ln -sf /taiga-media media
