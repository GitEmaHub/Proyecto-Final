from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.forms import *
from AppCoder.models import *
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


# Create your views here.


def inicioSesion(request):

    if request.method == "POST":

        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():

            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")

            user = authenticate(username = usuario, password = contra)

            if user:

                login(request, user)

                return render(request, "AppCoder/inicio.html", {"mensaje":f"Hola {user}"})

        else:

            return render(request, "AppCoder/inicio.html", {"mensaje":f"Los datos son incorrectos"})

    else:

        form = AuthenticationForm()

    return render(request, "AppCoder/login.html", {"fomLogin":form})


def registro(request):

    if request.method == "POST":

        form = UsuarioRegistro(request.POST)

        if form.is_valid():

            username = form.cleaned_data["username"]
            form.save()

            return render(request, "AppCoder/inicio.html", {"mensaje":"Usuario creado."})

    else:

        form = UsuarioRegistro()

    return render(request, "AppCoder/registro.html", {"fomLogin":form})


@login_required
def editarUsuario(request):

    usuario = request.user 

    if request.method == "POST":

        form = FormularioEditar(request.POST)

        if form.is_valid():

            info = form.cleaned_data

            usuario.email = info["email"]
            usuario.set_password(info["password1"])
            usuario.first_name = info["first_name"]
            usuario.last_name = info["last_name"]

            usuario.save()

            return render(request, "AppCoder/inicio.html")

    else:

        form = FormularioEditar(initial={
            "email":usuario.email,
            "first_name":usuario.first_name,
            "last_name":usuario.last_name,
        })

    return render(request, "AppCoder/editarPerfil.html", {"formulario":form, "usuario":usuario})


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



class ListaComunidad(LoginRequiredMixin, ListView):

    model = Comunidad

class DetalleComunidad(LoginRequiredMixin, DetailView):

    model = Comunidad

class CrearComunidad(LoginRequiredMixin, CreateView):

    model = Comunidad
    success_url = "/AppCoder/comunidad/list"
    fields = ["nombre", "apellido"]

class ActualizarComunidad(LoginRequiredMixin, UpdateView):

    model = Comunidad
    success_url = "/AppCoder/comunidad/list"
    fields = ["nombre", "apellido"]

class BorrarComunidad(LoginRequiredMixin, DeleteView):

    model = Comunidad
    success_url = "/AppCoder/comunidad/list"
    


@login_required
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

@login_required
def eliminarContactos(request, contactoNombre):

    contacto = Contacto.objects.get(nombre=contactoNombre)
    contacto.delete()

    contactos = Contacto.objects.all()

    contexto = {"personas":contactos}

    return render(request, "AppCoder/leerContactos.html", contexto)

@login_required
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






