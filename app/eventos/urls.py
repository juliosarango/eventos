from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

app_name = "eventos"

urlpatterns = [
    path(
        "nuevo",
        views.EventoNuevo.as_view(),
        name="nuevo",
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
