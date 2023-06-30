from django.shortcuts import render
from inicio.forms import CrearCleinte
from inicio.models import Cliente

# Create your views here.

def inicio(request):
    return render(request, 'inicio/inicio.html')

def crear_cliente(request):
    mensaje = ''
    
    if request.method == 'POST':
        formulario = CrearCleinte(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            cliente = Cliente(nombre=info['nombre'],edad=info['edad'],fecha_nacimiento=info['fecha_nacimiento'])
            cliente.save()
            mensaje = f'Se creó el cliente {cliente.nombre}'
        else:
            return render(request, 'inicio/crear_cliente.html', {'formulario': formulario})
    
    formulario = CrearCleinte()
    return render(request, 'inicio/crear_cliente.html', {'formulario': formulario, 'mensaje': mensaje})