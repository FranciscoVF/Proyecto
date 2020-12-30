from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Medicos, Servicios
from .forms import RegistroUsuarioForm, CrearServicio, RegistroMedicoForm


class DirectorSeccion(LoginRequiredMixin, UserPassesTestMixin, generic.TemplateView):
    template_name = "paginas/director.html"

    def test_func(self):
        return self.request.user.is_superuser


## CREATE ##
class CreateServicios(LoginRequiredMixin, CreateView):
    template_name = "paginas/crear_servicio.html"
    model = Servicios
    form_class = CrearServicio
    success_url = reverse_lazy('Medicos:Seccion_Director')

    def test_func(self):
        return self.request.user.is_superuser


class UsuarioRegistro(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = User
    template_name = "paginas/crear_usuario.html"
    form_class = RegistroUsuarioForm
    success_url = reverse_lazy('Medicos:Seccion_Director')

    def test_func(self):
        return self.request.user.is_superuser


class MedicoRegistro(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Medicos
    template_name = "paginas/crear_medico.html"
    form_class = RegistroMedicoForm
    success_url = reverse_lazy('Medicos:Seccion_Director')

    def test_func(self):
        return self.request.user.is_superuser


## READ ##
class ListMedicos(generic.ListView):
    template_name = "paginas/list_medicos.html"
    queryset = Medicos.objects.all().order_by('id')


class ListServicios(generic.ListView):
    template_name = "paginas/list_servicios.html"
    queryset = Servicios.objects.all().order_by('id')


class DListMedicos(LoginRequiredMixin, UserPassesTestMixin, generic.ListView):
    template_name = "paginas/dlista_medicos.html"
    queryset = Medicos.objects.all().order_by('id')

    def test_func(self):
        return self.request.user.is_superuser


class DListServicios(LoginRequiredMixin, UserPassesTestMixin, generic.ListView):
    template_name = "paginas/dlista_servicios.html"
    queryset = Servicios.objects.all().order_by('id')

    def test_func(self):
        return self.request.user.is_superuser


## UPDATE ##
class DirectorUpdateMedico(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    template_name = "paginas/actualizar_medico.html"
    model = Medicos
    form_class = RegistroMedicoForm
    success_url = reverse_lazy('Medicos:DLista_Medicos')

    def test_func(self):
        return self.request.user.is_superuser


class DirectorUpdateServicio(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    template_name = "paginas/actualizar_servicio.html"
    model = Servicios
    form_class = CrearServicio
    success_url = reverse_lazy('Medicos:DLista_Servicios')

    def test_func(self):
        return self.request.user.is_superuser


## DELETE ##
class EliminarMedico(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    template_name = "paginas/eliminar_medico.html"
    model = Medicos
    form_class = RegistroMedicoForm
    success_url = reverse_lazy('Medicos:DLista_Medicos')

    def test_func(self):
        return self.request.user.is_superuser


class EliminarServicio(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    template_name = "paginas/eliminar_servicio.html"
    model = Servicios
    form_class = CrearServicio
    success_url = reverse_lazy('Medicos:DLista_Servicios')

    def test_func(self):
        return self.request.user.is_superuser