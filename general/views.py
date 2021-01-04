from django.shortcuts import render
from django.views import generic

# Create your views here.
class Home(generic.TemplateView):
    template_name = "paginas/home.html"

class Informacion(generic.TemplateView):
    template_name = "paginas/informacion.html"