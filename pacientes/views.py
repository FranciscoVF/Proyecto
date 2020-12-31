from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Pacientes, Cita, Receta
from .forms import PacientesForm, CitasForm, RecetaForm
# Create your views here.

class CrearConsulta(LoginRequiredMixin,UserPassesTestMixin, CreateView):
    template_name = "consultas/paciente_consulta.html"
    model = Pacientes
    form_class = PacientesForm
    success_url = reverse_lazy('Pacientes:Crear_Consulta')

    def test_func(self):
        return self.request.user.is_active

class CrearCita(LoginRequiredMixin,UserPassesTestMixin, CreateView):
    template_name = "consultas/crear_cita.html"
    model = Cita
    form_class = CitasForm
    success_url = reverse_lazy('Pacientes:Crear_Cita')

    def test_func(self):
        return self.request.user.is_active

class CrearReceta(LoginRequiredMixin,UserPassesTestMixin, CreateView):
    template_name = "consultas/crear_receta.html"
    model = Receta
    form_class = RecetaForm
    success_url = reverse_lazy('Pacientes:Crear_Receta')

    def test_func(self):
        return self.request.user.is_active