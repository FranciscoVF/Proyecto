from django.contrib import admin
from django.urls import path,include
from Medicos.views import MedicoRegistro, DirectorSeccion

app_name='Medicos'
urlpatterns = [
    path('registrarMedico/',MedicoRegistro.as_view(),name='Medico_Registrar'),
    path('director/', DirectorSeccion.as_view(), name="Seccion_Director"),

]