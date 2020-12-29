from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Servicios, Medicos


class RegistroUsuarioForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
        ]

        labels = {
            'username': 'Nombre de Usuario',
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'email': 'Correo',
        }

class CrearServicio(forms.ModelForm):
    class Meta:
        model = Servicios
        fields = [
        "nombre",
        "descripcion"
        ]

class RegistroMedicoForm(forms.ModelForm):
    class Meta:
        model = Medicos
        fields = [
            'medico',
            'nombre',
            'apellido_p',
            'apellido_m',
            'servicio',
            'entrada',
            'salida',
            'dias_de_trabajo',
        ]