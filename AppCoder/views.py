from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Comunidad

# Create your views here.

def inicio(request):
    return render(request, "AppCoder/inicio.html")


def about(request): 
    return render(request, "AppCoder/about.html")


def latestWork(request): 
    return render(request, "AppCoder/comunidad.html")


def comunidad(request): 

    comu1 = Comunidad(nombre="Heberto", apellido="Alvarez")
    comu1.save()

    return HttpResponse(f"Esta es la comunidad que he creado: {comu1.nombre} y su apellido: {comu1.apellido}.")


def contacto(request): 
    return render(request, "AppCoder/contacto.html")

