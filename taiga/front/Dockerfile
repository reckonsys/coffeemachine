FROM nginx:alpine

ARG TAIGA_SCHEME
ARG TAIGA_VERSION
ARG TAIGA_BACK_HOST
ARG TAIGA_EVENTS_HOST
ARG TAIGA_EVENTS_SCHEME

WORKDIR /srv/taiga

RUN apk --no-cache add git \
	&& rm /etc/nginx/conf.d/default.conf \
	&& mkdir /run/nginx \
	&& git clone --depth=1 -b $TAIGA_VERSION-stable https://github.com/taigaio/taiga-front-dist.git front && cd front \
    && apk del git \
	&& rm dist/conf.example.json

WORKDIR /srv/taiga/front/dist

COPY nginx.conf /etc/nginx/conf.d/
COPY conf.json conf.json

RUN sed -e "s/TAIGA_SCHEME/${TAIGA_SCHEME}/g" \
		-e "s/TAIGA_BACK_HOST/${TAIGA_BACK_HOST}/g" \
		-e "s/TAIGA_EVENTS_SCHEME/${TAIGA_EVENTS_SCHEME}/g" \
		-e "s/TAIGA_EVENTS_HOST/${TAIGA_EVENTS_HOST}/g" \
		-i conf.json
