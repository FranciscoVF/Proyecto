from django import forms
from django.contrib.auth.models import User
from .models import Pacientes, Cita, Receta

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


class CitasForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = [
            'creada_por',
            'servicio',
            'nombre_paciente',
            'dia_hora_cita',
        ]

class RecetaForm(forms.ModelForm):
    class Meta:
        model = Receta
        fields = [
            'creada_por',
            'medicina',
            'nombre_paciente',
            'fecha_vencimiento',
            'descripcion',
        ]

class ImpRecetaForm(forms.ModelForm):
    class Meta:
        model = Receta
        fields = [
            'id',
            'creada_por',
            'medicina',
            'nombre_paciente',
            'fecha_vencimiento',
            'descripcion',
        ]