from django.contrib import admin
from .models import Categoria, Descripcion
# Register your models here.
class CategoriaAdmin(admin.ModelAdmin):
  readonly_fields =('created','updated')

class DescripcionAdmin(admin.ModelAdmin):
  readonly_fields =('created','updated')

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Descripcion, DescripcionAdmin)