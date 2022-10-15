from django import forms

class ComunidadFormulario(forms.Form):

    nombre = forms.CharField()
    apellido = forms.CharField() 