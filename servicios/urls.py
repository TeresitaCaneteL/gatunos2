from django.urls import path
from servicios.views import ServicioView

app_name="servicios"

urlpatterns=[
  path('servicio/', ServicioView.as_view(), name="servicio"),
  #path('registro/', registro, name="registro"),
]