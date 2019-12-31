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

#CHANGE_NOTIFICATIONS_MIN_INTERVAL = 300 #seconds
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
DEFAULT_FROM_EMAIL = environ['DEFAULT_FROM_EMAIL']
EMAIL_USE_TLS = environ['EMAIL_USE_TLS'] == '1'
EMAIL_USE_SSL = environ['EMAIL_USE_SSL'] == '1'
EMAIL_HOST = environ['EMAIL_HOST']
EMAIL_PORT =  int(environ['EMAIL_PORT'])
EMAIL_HOST_USER = environ['EMAIL_HOST_USER']
EMAIL_HOST_PASSWORD = environ['EMAIL_HOST_PASSWORD']

EVENTS_PUSH_BACKEND = "taiga.events.backends.rabbitmq.EventsPushBackend"
RABBIT_HOST=environ['RABBIT_HOST']
RABBIT_VHOST=environ['RABBITMQ_DEFAULT_VHOST']
EVENTS_PUSH_BACKEND_OPTIONS = {
    "url": f"amqp://guest:guest@{RABBIT_HOST}:5672/{RABBIT_VHOST}"}

PUBLIC_REGISTER_ENABLED = True
USER_EMAIL_ALLOWED_DOMAINS = ["reckonsys.com", "reckonsys.xyz"]
