from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Pacientes, Cita, Receta
from .forms import PacientesForm, CitasForm, RecetaForm
from Medicos.models import Servicios, Medicos


# Create your views here.

class CrearConsulta(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    template_name = "consultas/paciente_consulta.html"
    model = Pacientes
    form_class = PacientesForm
    success_url = reverse_lazy('Pacientes:Crear_Consulta')

    def test_func(self):
        return self.request.user.is_active


class CrearCita(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    template_name = "consultas/crear_cita.html"
    model = Cita
    form_class = CitasForm
    success_url = reverse_lazy('Pacientes:Crear_Cita')

    def test_func(self):
        return self.request.user.is_active


class CrearReceta(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    template_name = "consultas/crear_receta.html"
    model = Receta
    form_class = RecetaForm
    success_url = reverse_lazy('Pacientes:Crear_Receta')

    def test_func(self):
        return self.request.user.is_active


def MedicoConsultarCitas(request, pk):
    context = {
        "citas": Cita.objects.filter(servicio=pk).order_by('id')
    }
    return render(request, "consultas/list_cita_area.html", context)


class BitacorasSeccion(LoginRequiredMixin, UserPassesTestMixin, generic.TemplateView):
    template_name = "consultas/director_bitacoras.html"

    def test_func(self):
        return self.request.user.is_superuser

#def DirectorListaRecetas(request):
#    template = "consultas/dlist_recetas.html"
 #   context = {
  #      "recetas": Receta.objects.order_by('-fecha_creada')
   # }
    #return render(request, template, context)

class DirectorListaRecetas(LoginRequiredMixin, UserPassesTestMixin, generic.ListView):
    template_name = "consultas/dlist_recetas.html"
    model = Receta
    queryset = Receta.objects.all().order_by('fecha_creada')

    def test_func(self):
        return self.request.user.is_superuser

class DirectorListaPacientes(LoginRequiredMixin, UserPassesTestMixin, generic.ListView):
    template_name = "consultas/dlist_pacientes.html"
    model = Pacientes
    queryset = Pacientes.objects.all().order_by('hora_atendido')

    def test_func(self):
        return self.request.user.is_superuser


class DirectorListaCitas(LoginRequiredMixin, UserPassesTestMixin, generic.ListView):
    template_name = "consultas/dlist_citas.html"
    model = Cita
    queryset = Cita.objects.all().order_by('fecha_creada')

    def test_func(self):
        return self.request.user.is_superuser