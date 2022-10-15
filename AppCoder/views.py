from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.forms import *
from AppCoder.models import *

# Create your views here.

def inicio(request):
    return render(request, "AppCoder/inicio.html")


def about(request): 
    return render(request, "AppCoder/about.html")


def latestWork(request): 
    return render(request, "AppCoder/latestWork.html")


def comunidad(request): 

    comu1 = Comunidad(nombre="Heberto", apellido="Alvarez")
    comu1.save()

    return HttpResponse(f"Esta es la comunidad que he creado: {comu1.nombre} y su apellido: {comu1.apellido}.")


def contacto(request): 
    return render(request, "AppCoder/contacto.html")


def comuniFormulario(request):

    if request.method == "POST":

        comunidad1 = ComunidadFormulario(request.POST)
        
        if comunidad1.is_valid():

            info = comunidad1.cleaned_data

            comunidad = Comunidad(nombre=info["nombre"], apellido=info["apellido"])

            comunidad.save()

            return render(request, "AppCoder/inicio.html")

    else:

        comunidad1 = ComunidadFormulario()

        
    return render(request, "AppCoder/comuniFormulario.html", {"comu1":comunidad1})


def busquedaComunidad(request):

    return render(request, "AppCoder/busquedaComunidad.html")


def resultados(request):

    if request.GET["nombre"]:

        nombre = request.GET["nombre"]
        nombres = Comunidad.objects.filter(nombre__iexact=nombre)

        return render(request, "AppCoder/resultados.html", {"nombres":nombres, "nombre":nombre})

    else:
        respuesta = "No enviaste datos."

    return HttpResponse(respuesta)



