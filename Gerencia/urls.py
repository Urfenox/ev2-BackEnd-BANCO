from django.urls import path

from Gerencia import views as app

urlpatterns = [
    path('', app.mostrarInicio),
    path('editar/', app.mostrarEditor),
    path('eliminar/', app.hacerEliminacion),
    path('agregar/', app.mostrarAgregar)
]
