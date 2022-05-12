from django.urls import path
from app1.views import Home,registro,Adopcion

app_name="app1"

urlpatterns=[
  path('', Home.as_view(), name="index"),
  path('adopcion/', Adopcion.as_view(), name="adopcion"),
  path('registro/', registro, name="registro"),
]