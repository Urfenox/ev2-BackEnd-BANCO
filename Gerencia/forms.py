from django import forms
from .models import Solicitud

def AutoINcrementa():
    return Solicitud.objects.all().count() + 1

class AgregarSolicitud(forms.Form):
    # Creamos los campos del formulario y su tipo
    sId = forms.IntegerField()
    nombre = forms.CharField(required=True)
    cantidad = forms.IntegerField(required=True)
    fecha = forms.DateField()
    # Definimos atributos para los controles
    sId.widget.attrs['readonly'] = True
    sId.widget.attrs['value'] = AutoINcrementa()
    sId.widget.attrs['class'] = "form-control"
    nombre.widget.attrs['class'] = "form-control"
    cantidad.widget.attrs['class'] = "form-control"
    fecha.widget.attrs['class'] = "form-control"
