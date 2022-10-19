from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ComunidadFormulario(forms.Form):

    nombre = forms.CharField()
    apellido = forms.CharField() 


class ContactoFormulario(forms.Form):
    
    nombre = forms.CharField()
    apellido = forms.CharField()
    correo = forms.EmailField()
    
class UsuarioRegistro(UserCreationForm):

    password1 = forms.CharField(label = "Contrasena", widget=forms.PasswordInput)
    password2 = forms.CharField(label = "Repetir la contrasena", widget=forms.PasswordInput)
    email = forms.EmailField()

    class Meta:

        model = User
        fields = ["username", "password1", "password2", "email"]


class FormularioEditar(UserCreationForm):

    password1 = forms.CharField(label = "Contrasena", widget=forms.PasswordInput)
    password2 = forms.CharField(label = "Repetir la contrasena", widget=forms.PasswordInput)
    email = forms.EmailField()

    class Meta:

        model = User
        fields = ["password1", "password2", "email"]



