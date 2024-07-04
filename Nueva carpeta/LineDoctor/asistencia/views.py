from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def inicio(request):
    return HttpResponse(request,'inicio.urls')

def Bienvenidos(request):
    return render(request,'Bienvenidos.html')