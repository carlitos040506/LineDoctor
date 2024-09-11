from django.shortcuts import render, redirect, get_object_or_404
from .models import Paciente, Solicitud, Especialidad # Usa la primera letra en mayúscula
from django.contrib import messages

# Vista para la página de inicio
def home(request):
    return render(request, "home.html")
def pacientes(request):
    pacientes_listados = Paciente.objects.all() 
    messages.success(request, '¡Pacientes Listados!')
    return render(request, 'gestionpacientes.html', {"pacientes": pacientes_listados})

# Vista para registrar un paciente
def registrarpaciente(request):
    if request.method == 'POST':
        cedula = request.POST.get('txtCedula')
        nombre = request.POST.get('txtNombre')
        apellido = request.POST.get('txtApellido')
        email = request.POST.get('txtEmail')
        dia = request.POST.get('numdia')
        mes = request.POST.get('nummes')
        anio = request.POST.get('numanio')

        

        # Verificar si ya existe un paciente con la misma cédula
        if Paciente.objects.filter(cedula=cedula).exists():
            messages.error(request, '¡La cédula ya está registrada!')
            return redirect('gestionpacientes.html')
        else:
            # Crear el paciente con Paciente.objects.create
            Paciente.objects.create(cedula=cedula, nombre=nombre, apellido=apellido, email=email, dia=dia, mes=mes, anio=anio)
            messages.success(request, '¡Paciente registrado!')
            return redirect('gestionpacientes.html')

# Vista para editar un paciente
def edicionpaciente(request, cedula): 
    paciente = Paciente.objects.get(cedula=cedula)
    return render(request, "edicionpaciente.html", {"paciente": paciente})

def eliminarpaciente(request, cedula):
    paciente = Paciente.objects.get(cedula=cedula)
    paciente.delete()
    messages.success(request, '¡Paciente eliminado!')
    return redirect('gestionpacientes.html')
      

def editarpaciente(request):
    cedula = request.POST.get('txtCedula')
    nombre = request.POST.get('txtNombre')
    apellido = request.POST.get('txtApellido')
    email = request.POST.get('txtEmail')
    dia = request.POST.get('numdia')
    mes = request.POST.get('nummes')
    anio = request.POST.get('numanio')

    

    paciente = Paciente.objects.get(cedula=cedula)
    paciente.nombre = nombre
    paciente.apellido = apellido
    paciente.email = email
    paciente.dia = dia
    paciente.mes = mes
    paciente.anio = anio
    paciente.save()
    
    messages.success(request, '¡Paciente editado!')
    return redirect('gestionpacientes.html')


def solicitudes(request):
    solicitudes_listadas = Solicitud.objects.all() 
    messages.success(request, '¡Solicitudes Listadas!')
    return render(request, 'gestionsolicitud.html', {"solicitudes": solicitudes_listadas})

def registrarsolicitud(request):
    if request.method == 'POST':

        cedula = request.POST.get('txtCedula')
        nivel_dolor = request.POST.get('numniveldolor')
        especialidad = request.POST.get('txtEspecialidad')

        

        # Verificar si ya existe un paciente con la misma cédula
        if Solicitud.objects.filter(cedula=cedula).exists():
            messages.error(request, '¡La cédula ya tiene una solicitud')
            return redirect('/')
        else:
            # Crear el paciente con Paciente.objects.create
            Solicitud.objects.create(cedula=cedula, nivel_dolor=nivel_dolor, especialidad=especialidad)
            messages.success(request, '¡Solicitud creada!')
            return redirect('/')

# Vista para editar un paciente
def edicionsolicitud(request, cedula): 
    solicitud = Solicitud.objects.get(cedula=cedula)
    return render(request, "edicionsolicitud.html", {"solicitud": solicitud})

def eliminarsolicitud(request, cedula):
    solicitud = Solicitud.objects.get(cedula=cedula)
    solicitud.delete()
    messages.success(request, '¡Solicitud eliminada!')
    return redirect('/')
      

def editarsolicitud(request):
    
    cedula = request.POST.get('txtCedula')
    nivel_dolor = request.POST.get('numniveldolor')
    especialidad = request.POST.get('txtEspecialidad')

    

    solicitud = Solicitud.objects.get(cedula=cedula)
    solicitud.nivel_dolor = nivel_dolor
    solicitud.especialidad = especialidad

    Solicitud.save()
    
    messages.success(request, '¡Solicitud editada!')
    return redirect('/')

def contacto(request):
    return render(request, "contacto.html")