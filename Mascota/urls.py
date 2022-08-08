from django.urls import path

from Mascota.views import buscar_refugio, busqueda_refugio,Ficha_refugio, Ficha_veterinaria, Padre, Index, buscar_ficha, busqueda_Vacuna, inicio,ficha_mascota,busqueda_mascota,buscar_mascota


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
    path("ficha-mascotas/",ficha_mascota,name="ficha-mascotas"),
    path("ficha-busqueda-mascota/", busqueda_mascota, name="ficha-busqueda-mascota"),
    path("buscar-mascota/",buscar_mascota,name="buscar-mascota"),
]
