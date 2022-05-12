from django.forms import ModelForm, widgets
from app1.models import SolicitudAdopcion
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):
  class Meta:
    model = User
    fields = ['username',"first_name","last_name","email","password1","password2"]
    widgets={
      'username': forms.TextInput(attrs={'placeholder':'rut','id': 'rutificador','oninput':'checkRut(this)','required':'true'}),

  }

class FormSolicitud(forms.ModelForm):

  class Meta:
    model = SolicitudAdopcion
    fields=['usuario','fecha','telefono','direccion','tipo_casa','edad','region','ciudad']

