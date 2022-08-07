from django.shortcuts import render, redirect
from django.http import HttpResponse
import datetime
from django.template import loader
from Mascota import Templates
from Mascota.models import Ficha_medica, Refugio
from Mascota.forms import Ficha_form, Refugio_form


def Padre (request):
    return render (request, "padre.html")

def Index (request):

    return render (request, "index.html")

def inicio (request):

    return render(request, "inicio.html")


def Ficha_veterinaria (request):

    if request.method == "POST":

        miFormulario = Ficha_form(request.POST)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data

            ficha = Ficha_medica(registro = data["registro"], vacunas = data["vacunas"], desparasitacion= data["desparasitacion"], castracion= data["castracion"], observaciones= data["observaciones"])

            ficha.save()

            # return redirect(inicio)

            return render (request, "index.html" , context ={})

    else:

        miFormulario = Ficha_form()    

    return render(request, "ficha_veterinaria.html", {"miFormulario" : miFormulario})


def busqueda_Vacuna (request):

    return render (request, "ficha_busqueda.html")


def buscar_ficha (request):

    if request.GET["registro"]:

        registro= request.GET["registro"]

        fichas= Ficha_medica.objects.filter(registro__icontains = registro)

        return render(request, "ficha_resultado.html", {"fichas": fichas,"registro": registro})
    else:
        respuesta ="No enviaste datos"

    return render (request, "inicio.html", {"respuesta": respuesta})


def Ficha_refugio (request):

    if request.method == "POST":

        miFormulario = Refugio_form(request.POST)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data

            ficha = Refugio(nombre = data["nombre"], telefono = data["telefono"], email= data["email"], direccion= data["direccion"])

            ficha.save()

            # return redirect(inicio)

            return render (request, "index.html" , context ={})

    else:

        miFormulario = Refugio_form()    

    return render(request, "ficha_refugio.html", {"miFormulario" : miFormulario})


def busqueda_refugio (request):

    return render (request, "ficha_busqueda_refugio.html")


def buscar_refugio (request):

    if request.GET["nombre"]:

        nombre= request.GET["nombre"]

        fichas= Refugio.objects.filter(nombre__icontains = nombre)

        return render(request, "ficha_resultado_refugio.html", {"fichas": fichas,"nombre": nombre})
    else:
        respuesta ="No enviaste datos"

    return render (request, "inicio.html", {"respuesta": respuesta})


#  Products.objects.create(
            #     vacuna1= form.cleaned_data['vacuna1'],
            #     vacuna2 = form.cleaned_data['vacuna2'],
            #     vacuna3 = form.cleaned_data['vacuna3'],
            #     desparasitacion = form.cleaned_data['desparasitacion']
            #     castracion = form.cleaned_data['castracion'],
            #     observaciones = form.cleaned_data['']           
            # )
    