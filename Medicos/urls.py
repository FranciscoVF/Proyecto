from django.contrib import admin
from django.urls import path,include
from Medicos.views import MedicoRegistro

app_name='Medicos'
urlpatterns = [
    path('registrarMedico/',MedicoRegistro.as_view(),name='Medico_Registrar'),
 ]