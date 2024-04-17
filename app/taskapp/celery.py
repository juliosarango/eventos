import os

from celery import Celery
from celery.schedules import crontab
from django.apps import AppConfig, apps
from django.conf import settings

if not settings.configured:
    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE",
        "app.settings",
    )

app = Celery("app")
app.config_from_object("django.conf:settings", namespace="CELERY")


class CeleryAppConfig(AppConfig):
    name = "taskapp"
    verbose_name = "Celery Config"

    def ready(self) -> None:
        installed_apps = [
            app_config.name
            for app_config in apps.get_app_configs()
            if app_config.name.startswith("app")
        ]
        app.autodiscover_tasks(lambda: installed_apps, force=True)
