from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView
from django.views.generic import detail,View
from django.views.generic.list import ListView
from categorias.models import Categoria, Descripcion
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login
from django.template import Template, Context

# Create your views here.

class DescripcionView(View):
  def get(self, request, *args, **kwargs):
    descripcion = Descripcion.objects.all()
    context={
      'descripcion': descripcion

     }
    return render(request, 'categoria.html', context)



def CategoriaView(request, categoria_id):
    categoria = Categoria.objects.get(id=categoria_id)
    descripcion = Descripcion.objects.filter(categorias=categoria)
    return render(request, 'filtro.html', {'categoria': categoria,'descripcion': descripcion})

def categorias(request):
    posts = Post.objects.all()
    categorias = Categoria.objects.all()
    return render(request, "filtro.html", {'categoria': categoria})