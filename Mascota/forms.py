from contextlib import nullcontext
from django import forms


class Ficha_form (forms.Form):
    
    registro = forms.IntegerField()
    vacunas = forms.CharField(max_length=100)
    desparasitacion = forms.CharField(max_length=100)
    castracion = forms.CharField(max_length=100)
    observaciones = forms.CharField(max_length= 200)

class Refugio_form (forms.Form):

    nombre = forms.CharField()
    telefono = forms.IntegerField()
    email = forms.EmailField()
    direccion = forms.CharField()