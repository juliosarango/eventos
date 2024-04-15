from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

app_name = "eventos"

urlpatterns = [
    path(
        "",
        views.ListarEvento.as_view(),
        name="index-eventos",
    ),
    path(
        "nuevo",
        views.CrearEvento.as_view(),
        name="nuevo",
    ),
    path(
        "detalle/<uuid:reference>",
        views.DetalleEvento.as_view(),
        name="detalle",
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
