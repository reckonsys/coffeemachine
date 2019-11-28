FROM node:alpine

ARG RABBITMQ_DEFAULT_VHOST
ARG RABBIT_HOST
ARG TAIGA_EVENTS_PORT
ARG TAIGA_SECRET

WORKDIR /usr/src/

RUN apk add --no-cache --virtual .build-dependencies git perl \
	&& git clone https://github.com/taigaio/taiga-events.git taiga-events && cd taiga-events \
	&& perl -0777 -pe 's/"devDependencies": \{.*?\},//s' -i package.json \
	&& apk del .build-dependencies \
	&& yarn --production && yarn global add coffeescript

WORKDIR /usr/src/taiga-events

COPY config.json .

RUN sed -e "s/RABBITMQ_DEFAULT_VHOST/${RABBITMQ_DEFAULT_VHOST}/g" \
        -e "s/RABBIT_HOST/${RABBIT_HOST}/g" \
        -e "s/TAIGA_EVENTS_PORT/${TAIGA_EVENTS_PORT}/g" \
        -e "s/TAIGA_SECRET/${TAIGA_SECRET}/g" \
		-i config.json
