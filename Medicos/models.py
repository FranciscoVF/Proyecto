from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Servicios(models.Model):
    nombre = models.CharField(max_length=50,unique = True, null = True)
    descripcion = models.CharField(max_length = 128, help_text = "En que consiste el servicio")

    def __str__(self):
        return self.nombre

class Medicos(models.Model):
    medico = models.ForeignKey(User, on_delete=models.CASCADE, null = True)
    nombre = models.CharField(max_length=50, null = True)
    apellido_p = models.CharField(max_length=50, help_text="Apellido paterno", null = True)
    apellido_m = models.CharField(max_length=50, help_text="Apellido materno", null = True)
    servicio = models.ForeignKey(Servicios, on_delete=models.CASCADE, null = True)
    entrada = models.IntegerField(null=True, help_text="Formato de 24 horas")
    salida = models.IntegerField(null=True, help_text="Formato de 24 horas")
    dias_de_trabajo = models.CharField(max_length=50, null=True, help_text="Todos los dias que se va trabajar")

    def __str__(self):
        return self.nombre