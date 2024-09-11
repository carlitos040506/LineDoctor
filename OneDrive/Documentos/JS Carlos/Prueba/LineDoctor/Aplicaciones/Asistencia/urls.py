from django.urls import path
from . import views

urlpatterns =[
    path('', views.home, name='home'),  # Agrega un nombre para la ruta 'home'
    path('pacientes/', views.pacientes, name='pacientes'),
    path('registrarpaciente/', views.registrarpaciente, name='registrarPaciente'),  # Agrega un nombre para la ruta 'registrarPaciente'
    path('edicionpaciente/<cedula>', views.edicionpaciente),
    path('eliminarpaciente/<cedula>', views.eliminarpaciente), 
    path('editarpaciente/', views.editarpaciente),
    path('solicitudes/', views.solicitudes, name='solicitudes'),
    path('registrarsolicitud/', views.registrarsolicitud, name='registrarPaciente'),  # Agrega un nombre para la ruta 'registrarPaciente'
    path('edicionsolicitud/<cedula>', views.edicionsolicitud),
    path('eliminarsolicitud/<cedula>', views.eliminarsolicitud), 
    path('editarsolicitud/', views.editarsolicitud),
    path('contacto/', views.contacto, name='contacto'),
]