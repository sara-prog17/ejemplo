from django.shortcuts import render,redirect
from .forms import RutaForm

# Create your views here.
def index(request):
    nombre = 'pepito'
    return render(request,'index.html',{'nombre':nombre})

def formularioRuta(request):
    if request.method == 'POST':
        formulario = RutaForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            context = {
            'formulario': formulario
            }
            return render(request,'servigou/ruta.html',context)
    else:
        formulario = RutaForm()
        context = {
            'formulario': formulario
        }
        return render(request,'servigou/ruta.html',context)