from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Servicios(models.Model):
    nombre = models.CharField(max_length=50,unique = True, null = True)
    descripcion = models.CharField(max_length = 128, help_text = "En que consiste el servicio")

    def __str__(self):
        return self.nombre

class Medicos(models.Model):
    medico = models.ForeignKey(User, on_delete=models.CASCADE, null = True, help_text="Usuario asignado a medico")
    nombre = models.CharField(max_length=50, null = True,help_text="Nombre completo de usuario")
    apellido_p = models.CharField(max_length=50, help_text="Apellido paterno", null = True)
    apellido_m = models.CharField(max_length=50, help_text="Apellido materno", null = True)
    servicio = models.ForeignKey(Servicios, on_delete=models.CASCADE, null = True)
    entrada = models.CharField(null=True,max_length=50, help_text="Hora de entrada")
    salida = models.CharField(null=True,max_length=50, help_text="Hora de salida")
    dias_de_trabajo = models.CharField(max_length=50, null=True, help_text="Todos los dias que se va trabajar")

    def __str__(self):
        return self.nombre