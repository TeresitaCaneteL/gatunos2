from django.urls import path
from . import views
from categorias.views import DescripcionView,CategoriaView

app_name="categorias"

urlpatterns=[
  path('descripcion/', DescripcionView.as_view(), name="descripcion"),
  path('categoria/<int:categoria_id>/', views.CategoriaView, name="categoria"),


]