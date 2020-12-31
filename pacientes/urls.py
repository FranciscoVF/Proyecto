from django.contrib import admin
from django.urls import path,include
from .views import CrearConsulta, CrearCita, CrearReceta, MedicoConsultarCitas

app_name='Pacientes'

urlpatterns = [
    path('crearConsulta/', CrearConsulta.as_view(), name="Crear_Consulta"),
    path('crearCita/', CrearCita.as_view(), name="Crear_Cita"),
    path('crearReceta/', CrearReceta.as_view(), name="Crear_Receta"),

    path('consultarCitas/<int:pk>/', MedicoConsultarCitas, name="Consultar_citas"),

]