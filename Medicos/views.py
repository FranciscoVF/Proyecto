from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from Medicos.forms import RegistroForm
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Medicos

class MedicoRegistro(CreateView):
	model = User
	template_name = "paginas/registroMedico.html"
	form_class = RegistroForm

class DirectorSeccion(LoginRequiredMixin,UserPassesTestMixin,generic.TemplateView):
	template_name = "paginas/director.html"
	def test_func(self):
		return self.request.user.is_superuser


## CREATE ##

## READ ##
class ListMedicos(generic.ListView):
    template_name = "paginas/list_medicos.html"
    queryset = Medicos.objects.all().order_by('id')

class ListServicios(generic.ListView):
	template_name = "paginas/list_servicios.html"
	queryset = Medicos.objects.all().order_by('id')

## UPDATE ##

## DELETE ##