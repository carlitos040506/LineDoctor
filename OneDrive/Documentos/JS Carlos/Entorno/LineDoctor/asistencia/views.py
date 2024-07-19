from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Bienvenidos a LineDoctor Asistencia")
    
# Create your views here.

def nosotros(request):
    return render(request, 'paginas/nosotros.html')


def index(request):
    return render(request, 'estudiantes/index.html')

def crear(request):
    return render(request, 'estudiantes/crear.html')

def editar(request):
    return render(request, 'estudiantes/editar.html')

def registro(request):
    return render(request, 'paginas/registro.html')