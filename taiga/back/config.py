from .common import *
from os import environ

DEBUG = False
TEMPLATE_DEBUG = False

SECRET_KEY = environ.get('TAIGA_SECRET', 'not-so-secret')
SCHEME = environ.get('TAIGA_SCHEME')
HOST = environ.get('TAIGA_BACK_HOST')

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
        "NAME": environ.get('POSTGRES_DB'),
        "HOST": environ.get("POSTGRES_HOST"),
        "USER": environ.get("POSTGRES_USER"),
        "PASSWORD": environ.get("POSTGRES_PASSWORD")
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
DEFAULT_FROM_EMAIL = environ.get('DEFAULT_FROM_EMAIL')
EMAIL_USE_TLS = environ.get('EMAIL_USE_TLS') == '1'
EMAIL_USE_SSL = environ.get('EMAIL_USE_SSL') == '1'
EMAIL_HOST = environ.get('EMAIL_HOST')
EMAIL_PORT =  int(environ.get('EMAIL_PORT', 0))
EMAIL_HOST_USER = environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = environ.get('EMAIL_HOST_PASSWORD')

EVENTS_PUSH_BACKEND = "taiga.events.backends.rabbitmq.EventsPushBackend"
RABBIT_HOST=environ.get('RABBIT_HOST')
RABBIT_VHOST=environ.get('RABBITMQ_DEFAULT_VHOST')
EVENTS_PUSH_BACKEND_OPTIONS = {
    "url": f"amqp://guest:guest@{RABBIT_HOST}:5672/{RABBIT_VHOST}"}

PUBLIC_REGISTER_ENABLED = False
MIDDLEWARE_CLASSES = ['whitenoise.middleware.WhiteNoiseMiddleware'] + MIDDLEWARE_CLASSES
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

INSTALLED_APPS = [
    'jet.dashboard',
    'jet',
] + INSTALLED_APPS
