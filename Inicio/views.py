from django.shortcuts import render

# Create your views here.

def mostrarInicio(request):
    return render(request, 'index.html')
