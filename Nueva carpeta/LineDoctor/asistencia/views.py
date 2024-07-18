from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import Template, context
# def inicio(request):
#     return HttpResponse(request,'inicio.urls')

# def bienvenidos(request):
#     doc=open("C:/Users/sergi/OneDrive/Documentos/JS Carlos/LineDoctor/Nueva carpeta/LineDoctor/asistencia/template/paginas/Bienvenidos.html")
#     h=Template(doc.read())
#     doc.close()
#     ctx=context()
#     saludo=h.render(ctx)
#     return HttpResponse(saludo)

def home(request):
    return render(request, 'Bienvenidos.html')