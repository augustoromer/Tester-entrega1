from django.urls import path

from Mascota.views import buscar_refugio, busqueda_refugio

from Mascota.views import Ficha_refugio, Ficha_veterinaria, Padre, Index, buscar_ficha, busqueda_Vacuna, inicio



urlpatterns = [
    path("index/", Index, name="index"),
    path("padre/", Padre, name="padre"),
    path("inicio/", inicio, name="inicio"),
    path("ficha-veterinaria/", Ficha_veterinaria, name="ficha-veterinaria"),
    path("ficha-busqueda/", busqueda_Vacuna, name="ficha-busqueda"),
    path("buscar/", buscar_ficha, name="buscar"),
    path("ficha-refugio/", Ficha_refugio, name="ficha-refugio"),
    path("ficha-busqueda-refugio/", busqueda_refugio, name="ficha-busqueda-refugio"),
    path("buscar-refugio/", buscar_refugio, name="buscar-refugio"),
]
