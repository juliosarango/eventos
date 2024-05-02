from .base import *

INSTALLED_APPS += ["debug_toolbar"]

MIDDLEWARE.insert(0, "debug_toolbar.middleware.DebugToolbarMiddleware")


# Email
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "30.10.10.42"
EMAIL_PORT = 1025
EMAIL_FROM = "info@test.com"

DOMAIN = "localhost:8000"
SITE_NAME = "Rifas y Eventos"
PROTOCOL = "http"

CELERY_BROKER_URL = "redis://30.10.10.41:6379"
CELERY_RESULT_BACKEND = "redis://30.10.10.41:6379"
