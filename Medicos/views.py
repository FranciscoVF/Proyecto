from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from Medicos.forms import RegistroForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

class MedicoRegistro(CreateView):
	model = User
	template_name = "paginas/registroMedico.html"
	form_class = RegistroForm

