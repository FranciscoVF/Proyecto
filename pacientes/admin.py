from django.contrib import admin
from .models import Pacientes, Cita, Receta
# Register your models here.

admin.site.register(Pacientes)
admin.site.register(Cita)
admin.site.register(Receta)