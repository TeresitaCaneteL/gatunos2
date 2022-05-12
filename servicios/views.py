from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import detail,View
from django.views.generic import TemplateView
from django.views.generic.edit import  FormView, UpdateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView
from django.views.generic.list import ListView
from servicios.models import Servicio
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login
from django.template import Template, Context

# Create your views here.

class ServicioView(View):
  def get(self, request, *args, **kwargs):
    servicio = Servicio.objects.all()
    context={
      'servicio':servicio

     }
    return render(request, 'servicios.html', context)

