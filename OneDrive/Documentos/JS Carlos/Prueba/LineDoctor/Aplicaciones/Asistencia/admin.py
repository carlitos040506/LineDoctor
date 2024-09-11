from django.contrib import admin
from .models import Paciente, Solicitud, Especialidad

# Register your models here.
admin.site.register(Paciente)
admin.site.register(Solicitud)
admin.site.register(Especialidad)