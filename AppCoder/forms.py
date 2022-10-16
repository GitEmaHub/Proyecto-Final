from django import forms

class ComunidadFormulario(forms.Form):

    nombre = forms.CharField()
    apellido = forms.CharField() 


class ContactoFormulario(forms.Form):
    
    nombre = forms.CharField()
    apellido = forms.CharField()
    correo = forms.EmailField()
    