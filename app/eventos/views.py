from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from .forms import EventoForm


class EventoNuevo(LoginRequiredMixin, CreateView):
    form_class = EventoForm
    template_name = "evento/nuevo.html"

    def post(self, request, *args, **kwargs):
        initial = {}

        form = self.form_class(request.POST, request.FILES)
        print(form.is_valid())
        print(form.errors)
        context = {"form": form}
        if form.is_valid():
            user = request.user            
            estado_publicacion = True if (int(request.POST["cantidad_boletos"]) < 500) else False

            evento = form.save(commit=False)
            evento.publicado = estado_publicacion
            evento.usuario = user
            evento.save()

        return render(request, self.template_name, context)
