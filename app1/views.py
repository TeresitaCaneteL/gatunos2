from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from app1.forms import CustomUserCreationForm, FormSolicitud
from django.views.generic import detail
from django.views.generic import TemplateView
from django.views.generic.edit import FormView, UpdateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView
from django.views.generic.list import ListView
from app1.models import SolicitudAdopcion
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login
from django.template import Template, Context

# Create your views here.
class Home(TemplateView):

  template_name = 'index.html'



def registro(request):
  data = {
    'form': CustomUserCreationForm()
  }
  if request.method == 'POST':
    formulario = CustomUserCreationForm(data=request.POST)
    if formulario.is_valid():
      formulario.save()
      user = authenticate(username=formulario.cleaned_data['username'], password=formulario.cleaned_data['password1'])
      login(request, user)
      messages.success(request,"registro exitoso")
      return redirect(to="index")
    data["form"]= formulario
  return render(request, 'registration/registro.html', data)

class Adopcion(CreateView):
  model = SolicitudAdopcion
  template_name = 'solicitudAdopcion.html'
  form_class = FormSolicitud
  success_url =reverse_lazy('app1:index')
  def post(self, request, *args, **kwargs):
    if request.method == 'POST':
      form = FormSolicitud(request.POST)
      request.POST['ciudad'].encode('utf-8')
      request.POST['region'].encode('utf-8')
      if form.is_valid():
        form.save()
        messages.success(request,"ingrese datos correctos")
        return redirect('app1:index')
      else:
        messages.success(request,"ingrese datos correctos")

    return redirect('app1:adopcion')