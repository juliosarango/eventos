from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.db.models import Q

from .forms import EventoForm
from utils.utils import Utils
from .models import Evento, Vendedor, Boletos


class ListarEvento(LoginRequiredMixin, ListView):
    def get(self, request, *args, **kwargs):

        user = request.user
        eventos = Evento.objects.filter(usuario=user)
        return render(
            request,
            "evento/index.html",
            context={"eventos": eventos},
        )


class DetalleEvento(LoginRequiredMixin, ListView):
    def get(self, request, *args, **kwargs):

        user = request.user
        reference = kwargs["reference"]
        evento = Evento.objects.get(Q(usuario=user), Q(reference=reference))
        vendedores = Vendedor()
        boletos = Boletos()
        if evento:
            vendedores = Vendedor.objects.filter(evento=evento)
            boletos = Boletos.objects.filter(evento=evento)
            if vendedores and boletos:
                return render(
                    request,
                    "evento/detalle.html",
                    context={
                        "evento": evento,
                        "vendedores": vendedores,
                        "boletos": boletos,
                    },
                )

        eventos = Evento.objects.filter(usuario=user)
        return render(
            request,
            "evento/index.html",
            context={"eventos": eventos},
        )


class CrearEvento(LoginRequiredMixin, CreateView):
    form_class = EventoForm
    template_name = "evento/nuevo.html"

    def post(self, request, *args, **kwargs):
        initial = {}

        form = self.form_class(request.POST, request.FILES)
        context = {"form": form}
        if form.is_valid():
            user = request.user
            cantidad_boletos = int(request.POST["cantidad_boletos"])
            estado_publicacion = True if (cantidad_boletos < 500) else False

            evento = form.save(commit=False)
            evento.publicado = estado_publicacion
            evento.usuario = user
            evento.save()

            if estado_publicacion:
                Utils.asignar_vendedor(self, evento=evento, usuario=user)
                Utils.generar_boletos(self, evento=evento, cantidad=cantidad_boletos)

        return render(request, self.template_name, context)
