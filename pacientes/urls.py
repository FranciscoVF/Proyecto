from django.contrib import admin
from django.urls import path,include
from .views import CrearConsulta, CrearCita, CrearReceta, MedicoConsultarCitas, BitacorasSeccion, \
    DirectorListaRecetas, DirectorListaPacientes, DirectorListaCitas
app_name='Pacientes'

urlpatterns = [
    path('listaBitacoras/', BitacorasSeccion.as_view(), name="Lista_Bitacoras"),

    path('crearConsulta/', CrearConsulta.as_view(), name="Crear_Consulta"),
    path('crearCita/', CrearCita.as_view(), name="Crear_Cita"),
    path('crearReceta/', CrearReceta.as_view(), name="Crear_Receta"),

    path('consultarCitas/<int:pk>/', MedicoConsultarCitas, name="Consultar_citas"),
    path('listaCitas/', DirectorListaRecetas.as_view(),name="Director_Lista_Recetas"),
    path('listaPacientes/', DirectorListaPacientes.as_view(),name="Director_Lista_Pacientes"),
    path('listaCitas/', DirectorListaCitas.as_view(),name="Director_Lista_Citas"),
]