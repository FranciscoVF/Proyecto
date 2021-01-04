from django.db import models
from django.contrib.auth.models import User
from Medicos.models import Servicios
# Create your models here.

class Pacientes(models.Model):
    atendiendo = models.ForeignKey(User, on_delete=models.CASCADE, null = True)
    nombre = models.CharField(max_length=50, null = True,help_text="Nombre completo del paciente")
    apellido_p = models.CharField(max_length=50, help_text="Apellido paterno", null = True)
    apellido_m = models.CharField(max_length=50, help_text="Apellido materno", null = True)
    edad = models.IntegerField(null = True)
    contacto = models.CharField(max_length=255, help_text="Manera por la cual nos podemos poner en contacto con paciente ya sea correo, celular o telefono de casa (esta seccion puede quedar vacia)", null = True)
    descripcion = models.CharField(max_length=255, help_text="De que trato la colsulta y seguimiento que se dara", null=True)
    hora_atendido = models.DateTimeField(auto_now_add=True, null = True)

    def __str__(self):
        return self.nombre


class Cita(models.Model):
    creada_por = models.ForeignKey(User, on_delete=models.CASCADE, null = True, related_name='Atendiendo')
    fecha_creada = models.DateTimeField(auto_now_add=True, null = True)
    servicio = models.ForeignKey(User,related_name='Especialista', on_delete=models.CASCADE, null = True, help_text="Usuario del especialista con el que sera mandado")
    nombre_paciente = models.CharField(max_length=50, null = True,help_text="Nombre completo del paciente")
    dia_hora_cita = models.DateTimeField(null=True,max_length=50, help_text="Dia y hora de cita.Formato AAAA-MM-DD H-M-S Ejemplo: 2021-01-17 14:30")

    def __str__(self):
        return self.nombre_paciente


class Receta(models.Model):
    creada_por = models.ForeignKey(User, on_delete=models.CASCADE, null = True)
    fecha_creada = models.DateTimeField(auto_now_add=True, null = True)
    medicina = models.CharField(max_length=255, null=True, help_text="Medicina que se esta recetando")
    nombre_paciente = models.CharField(max_length=255, null = True,help_text="Nombre completo del paciente")
    fecha_vencimiento = models.DateTimeField(null=True, help_text="Hasta que fecha ser tiene para usar.Formato AAAA-MM-DD Ejemplo: 2021-01-17")
    descripcion = models.CharField(max_length=255, null=True, help_text="Detalles como cantidad y cada cuanto tomar")

    def __str__(self):
        return self.nombre_paciente