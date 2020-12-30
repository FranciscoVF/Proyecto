from django import forms
from django.contrib.auth.models import User
from .models import Pacientes

class PacientesForm(forms.ModelForm):
    class Meta:
        model = Pacientes
        fields = [
            'atendiendo',
            'nombre',
            'apellido_p',
            'apellido_m',
            'edad',
            'contacto',
            'descripcion',
        ]
