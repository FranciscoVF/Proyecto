from django.urls import path

from general import views

app_name = "paginas"

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('informacion', views.Informacion.as_view(), name="Informacion"),
]
