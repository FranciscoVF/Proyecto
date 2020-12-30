from django.contrib import admin
from django.urls import path,include
from .views import CrearConsulta

app_name='Pacientes'

urlpatterns = [
    path('crearConsulta/', CrearConsulta.as_view(), name="Crear_Consulta"),

]