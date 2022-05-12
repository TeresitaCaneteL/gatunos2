from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.
class SolicitudAdopcion(models.Model):
  tipo_domicilio=[
    (1,'departamento'),
    (2,'casa'),
    (3,'casa/patio'),
    (4,'parcela'),
  ]
  usuario = models.CharField(max_length=20)
  fecha = models.DateField()
  telefono = models.CharField(max_length=20)
  direccion = models.CharField(max_length=30)
  tipo_casa = models.IntegerField(blank=False, null=False, choices=tipo_domicilio,default='1')
  edad = models.IntegerField(blank=False, null=False)
  region = models.CharField(max_length=255)
  ciudad = models.CharField(max_length=255)

  def __str__(self):
      return '{}'.format(self.usuario)


