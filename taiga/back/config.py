from .common import *
from os import environ

PUBLIC_REGISTER_ENABLED = True
DEBUG = False
TEMPLATE_DEBUG = False

SECRET_KEY = environ['TAIGA_SECRET']
SCHEME = environ['TAIGA_SCHEME']
HOST = environ['TAIGA_BACK_HOST']

MEDIA_URL = f"{SCHEME}://{HOST}/media/"
STATIC_URL = f"{SCHEME}://{HOST}/static/"
ADMIN_MEDIA_PREFIX = f"{SCHEME}://{HOST}/static/admin/"
SITES["api"]["scheme"] = SCHEME
SITES["api"]["domain"] = HOST
SITES["front"]["scheme"] = SCHEME
SITES["front"]["domain"] = HOST

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": environ['POSTGRES_DB'],
        "HOST": environ["POSTGRES_HOST"],
        "USER": environ["POSTGRES_USER"],
        "PASSWORD": environ["POSTGRES_PASSWORD"]
    }
}

#DEFAULT_FROM_EMAIL = "john@doe.com"
#CHANGE_NOTIFICATIONS_MIN_INTERVAL = 300 #seconds
#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
#EMAIL_USE_TLS = False
#EMAIL_USE_SSL = False # You cannot use both (TLS and SSL) at the same time!
#EMAIL_HOST = 'localhost'
#EMAIL_PORT = 25
#EMAIL_HOST_USER = 'user'
#EMAIL_HOST_PASSWORD = 'password'

EVENTS_PUSH_BACKEND = "taiga.events.backends.rabbitmq.EventsPushBackend"
RABBIT_HOST=environ['RABBIT_HOST']
RABBIT_VHOST=environ['RABBITMQ_DEFAULT_VHOST']
EVENTS_PUSH_BACKEND_OPTIONS = {
    "url": f"amqp://guest:guest@{RABBIT_HOST}:5672/{RABBIT_VHOST}"}
