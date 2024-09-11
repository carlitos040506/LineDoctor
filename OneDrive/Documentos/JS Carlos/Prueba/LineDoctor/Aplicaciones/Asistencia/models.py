from django.db import models

# Create your models here.
from django.db import models

class Paciente(models.Model):
    cedula = models.CharField(max_length=20, primary_key=True)  # Usamos CharField para cedula si es un varchar en MySQL
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    dia = models.IntegerField()
    mes = models.IntegerField()
    anio = models.IntegerField()

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"

class Especialidad(models.Model):
    id = models.AutoField(primary_key=True)
    especialidad = models.CharField(max_length=100)

    def __str__(self):
        return self.especialidad

class Solicitud(models.Model):
    
    cedula = models.CharField(max_length=20, primary_key=True)  # Relación con Paciente
    especialidad = models.CharField(max_length=100)  # Relación con Especialidad
    nivel_dolor = models.IntegerField()

    def __str__(self):
        return f"Solicitud {self.id} - {self.cedula} - {self.especialidad}"
