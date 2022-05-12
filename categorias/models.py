from django.db import models

# Create your models here.
class Categoria(models.Model):
  nombreC = models.CharField(max_length=50)
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now_add=True)

  class Meta:
    verbose_name ='categoria'
    verbose_name_plural ='categorias'

  def __str__(self):
    return self.nombreC

class Descripcion(models.Model):
  nombre = models.CharField(max_length=50)
  descripcion =models.CharField(max_length=100)
  sexo =models.CharField(max_length=20)
  imagen = models.ImageField(upload_to='categoria')
  edad = models.IntegerField()
  categorias = models.ManyToManyField(Categoria)
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now_add=True)

  class Meta:
    verbose_name ='descripcion'
    verbose_name_plural ='descripciones'

  def __str__(self):
    return self.nombre