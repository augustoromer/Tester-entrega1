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

sexos = [(' Macho',' Macho'),(' Hembra',' Hembra')]
lista_especies = [(' Perro',' Perro'),(' Gato',' Gato')]
class Mascota_form (forms.Form):
    nickname = forms.CharField()
    especie = forms.ChoiceField(choices=lista_especies,required=True,label='Seleccione la especie')
    raza = forms.CharField()
    sexo =  forms.ChoiceField(choices=sexos,required=True,label='Seleccione el sexo')
    edad_aprox= forms.IntegerField(label='Edad aproximada')
    ingreso = forms.DateField()
    observaciones = forms.CharField()