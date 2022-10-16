from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.forms import *
from AppCoder.models import *
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


# Create your views here.

def inicio(request):
    return render(request, "AppCoder/inicio.html")


def about(request): 
    return render(request, "AppCoder/about.html")


def latestWork(request): 
    return render(request, "AppCoder/latestWork.html")


def comunidad(request): 

    return render(request, "AppCoder/comunidad.html")



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

    return render(request, "AppCoder/comunidad.html")


def resultados(request):

    if request.GET["nombre"]:

        nombre = request.GET["nombre"]
        nombres = Comunidad.objects.filter(nombre__iexact=nombre)

        return render(request, "AppCoder/comunidad.html", {"nombres":nombres, "nombre":nombre})

    else:
        respuesta = "No enviaste datos."

    return HttpResponse(respuesta)

    
def contacto(request): 
    return render(request, "AppCoder/contacto.html")



class ListaComunidad(ListView):

    model = Comunidad

class DetalleComunidad(DetailView):

    model = Comunidad

class CrearComunidad(CreateView):

    model = Comunidad
    success_url = "/AppCoder/comunidad/list"
    fields = ["nombre", "apellido"]

class ActualizarComunidad(UpdateView):

    model = Comunidad
    success_url = "/AppCoder/comunidad/list"
    fields = ["nombre", "apellido"]

class BorrarComunidad(DeleteView):

    model = Comunidad
    success_url = "/AppCoder/comunidad/list"
    



def leerContactos(request):

    contactos = Contacto.objects.all()

    contexto = {"personas": contactos}

    return render(request, "AppCoder/leerContactos.html", contexto)

def crearContactos(request):

    if request.method == "POST":

        miFormulario = ContactoFormulario(request.POST)
        
        if miFormulario.is_valid():

            info = miFormulario.cleaned_data

            contacto = Contacto(nombre=info["nombre"], apellido=info["apellido"], correo=info["correo"])

            contacto.save()

            return render(request, "AppCoder/inicio.html")

    else:

        miFormulario = ContactoFormulario()

        
    return render(request, "AppCoder/contactoFormulario.html", {"miFormulario":miFormulario})


def eliminarContactos(request, contactoNombre):

    contacto = Contacto.objects.get(nombre=contactoNombre)
    contacto.delete()

    contactos = Contacto.objects.all()

    contexto = {"personas":contactos}

    return render(request, "AppCoder/leerContactos.html", contexto)


def editarContactos(request, contactoNombre):

    contacto = Contacto.objects.get(nombre=contactoNombre)
    
    if request.method == "POST":

        miFormulario = ContactoFormulario(request.POST)
        
        if miFormulario.is_valid():

            info = miFormulario.cleaned_data

            contacto.nombre = info["nombre"]
            contacto.apellido = info["apellido"]
            contacto.correo = info["correo"]

            contacto.save()

            return render(request, "AppCoder/inicio.html")

    else:

        miFormulario = ContactoFormulario(initial={"nombre":contacto.nombre, "apellido":contacto.apellido, "correo":contacto.correo})

        
    return render(request, "AppCoder/editarContacto.html", {"miFormulario":miFormulario, "nombre":contactoNombre})






