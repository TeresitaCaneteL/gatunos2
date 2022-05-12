from django.db import models

# Create your models here.
class Servicio(models.Model):
  nombre = models.CharField(max_length=50)
  raza = models.CharField(max_length=50)
  descripcion =models.CharField(max_length=100)
  sexo =models.CharField(max_length=20)
  imagen = models.ImageField(upload_to='servicios')
  edad = models.IntegerField()
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now_add=True)

  class Meta:
    verbose_name ='servicio'
    verbose_name_plural ='servicios'

  def __str__(self):
    return self.nombre