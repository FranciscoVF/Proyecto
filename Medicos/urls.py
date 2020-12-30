from django.contrib import admin
from django.urls import path,include
from .views import UsuarioRegistro, DirectorSeccion, ListMedicos, \
    ListServicios, CreateServicios, MedicoRegistro, DListMedicos, \
    DListServicios, DirectorUpdateMedico

app_name='Medicos'
urlpatterns = [

    path('director/', DirectorSeccion.as_view(), name="Seccion_Director"),

    path('listMedicos/', ListMedicos.as_view(), name="List_Medicos"),
    path('dListaMedicos/', DListMedicos.as_view(), name="DLista_Medicos"),
    path('listServicios/', ListServicios.as_view(), name="List_Servicios"),
    path('dListaServicios/', DListServicios.as_view(), name="DLista_Servicios"),

    path('usuarioRegistro/',UsuarioRegistro.as_view(),name='Usuario_Registrar'),
    path('crearServicio/', CreateServicios.as_view(), name= "Crear_Servicio"),
    path('medicoRegistro/', MedicoRegistro.as_view(), name= "Medico_Registrar"),

    path('dUpdateMedico/<int:pk>/', DirectorUpdateMedico.as_view(), name="DUpdate_Medico"),
]