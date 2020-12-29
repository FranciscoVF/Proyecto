from django.contrib import admin
from django.urls import path,include
from .views import MedicoRegistro, DirectorSeccion, ListMedicos, ListServicios, CreateServicios

app_name='Medicos'
urlpatterns = [
    path('registrarMedico/',MedicoRegistro.as_view(),name='Medico_Registrar'),
    path('director/', DirectorSeccion.as_view(), name="Seccion_Director"),

    path('listMedicos/', ListMedicos.as_view(), name="List_Medicos"),
    path('listServicios/', ListServicios.as_view(), name="List_Servicios"),

    path('crearServicio/', CreateServicios.as_view(), name= "Crear_Servicio"),
]