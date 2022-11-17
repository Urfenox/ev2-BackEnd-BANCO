from django.shortcuts import render, redirect
from .models import Solicitud
from datetime import datetime
from . import forms

# Create your views here.

def mostrarInicio(request):
    # Obtiene todos los objetos de la tabla 'Solicitud'
    solicitudes = Solicitud.objects.all()
    # Pone todos los objetos en una variable tipo diccionario 'data'
    data = {'solicitudes':solicitudes}
    # Devuelve el render del sitio index.html y pasa la variable 'data' al render
    return render(request, 'Gerencia\index.html', data)

def mostrarEditor(request):
    # identifica si la peticion es un POST
    if request.method == "POST":
        # Define variables con sus datos enviados desde el POST
        id = request.POST['id']
        nombre = request.POST['nombre']
        cantidad = request.POST['cantidad']
        # Convierte la fecha desde el formato entregado a YYYY/mm/dd
        fecha_ingreso = datetime.strptime(request.POST['fecha'], "%Y-%m-%d").date()
        # Crea un objeto tipo Solicitud y le pasa los valores recolectados
        s = Solicitud(id, nombre, cantidad, fecha_ingreso)
        # Guarda el objeto creado en la DB
        s.save()
        # NOTA:
        #   - Como la ID ya existe,
        #   entonces el registro que coincida
        #   con la ID se sobreescribira con los nuevos valores
        # al terminar, redirecciona al sitio inicio
        return redirect('../')
    else: # no es un POST. se debe mostrar el sitio.
        # Obtener el objeto de la tabla 'Solicitud' cuya id sea igual al GET('id')
        solicitud = Solicitud.objects.get(id=request.GET['id'])
        # Define una variable para pasar los datos a la vista
        data = {'solicitud':solicitud}
        return render(request, 'Gerencia/editar.html', data)

def hacerEliminacion(request):
    # Obtiene el objeto que coincide con la ID
    s = Solicitud.objects.get(id=request.GET['id'])
    # Lo elimina
    s.delete()
    return redirect('../')

def mostrarAgregar(request):
    # identifica si la peticion es un POST
    form = forms.AgregarSolicitud()
    # Verificamos si es un POST
    if request.method == "POST":
        # Obtenemos el formulario del POST
        form = forms.AgregarSolicitud(request.POST)
        # Checkeamos que el formulario sea valido
        if form.is_valid():
            # Creamos un objeto 'Solicitud' y lo habitamos
            #   con los datos del POST del formulario
            s = Solicitud(request.POST['sId'], request.POST['nombre'], request.POST['cantidad'], datetime.strptime(request.POST['fecha'], "%d/%m/%Y").date())
            # Guardamos el objeto en la DB
            s.save()
            # Redireccionamos a Inicio
            return redirect('../')
    data = {"form": form}
    return render(request, 'Gerencia\\agregar.html', data)
