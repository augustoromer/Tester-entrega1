from django.contrib import admin
from Mascota.models import  Mascota, Ficha_medica, Refugio
# Register your models here.


# class Usuario_admin(admin.ModelAdmin):
#     list_display = ["nombre","apellido","DNI","telefono","email",]

class Mascota_admin(admin.ModelAdmin):
    list_display = ["nickname","especie","raza","sexo","edad_aprox","ingreso"]

class Ficha_admin(admin.ModelAdmin):
    list_display = ["registro","vacunas","desparasitacion","castracion", "observaciones"]

class Refugio_admin(admin.ModelAdmin):
    list_display = ["nombre","telefono","email","direccion"]

# admin.site.register(Usuario, Usuario_admin)
admin.site.register(Mascota,Mascota_admin)
admin.site.register(Ficha_medica, Ficha_admin)
admin.site.register(Refugio, Refugio_admin)