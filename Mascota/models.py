from django.db import models

class Mascota (models.Model):

    nickname = models.CharField(max_length= 50, unique=True)
    especie = models.CharField(max_length= 50)
    raza = models.CharField(max_length= 50)
    sexo = models.CharField (max_length= 20)
    edad_aprox= models.IntegerField()
    ingreso = models.DateField()
    observaciones = models.TextField(max_length=80,null=True, blank=True)

    
    # relaciones con las otras clases: Usuario
    # persona = models.ForeignKey(Usuario, null=True, blank=True, on_delete=models.CASCADE)
    

    def __str__(self):
         return f" {self.nickname} - {self.especie} - {self.raza} - {self.sexo} - {self.edad_aprox} - {self.ingreso}"



# class Usuario (models.Model):

#     nombre = models.CharField(max_length= 50)
#     apellido = models.CharField(max_length= 50)
#     DNI = models.IntegerField(unique=True)
#     telefono = models.IntegerField(unique=True)
#     email = models.EmailField(unique=True)

#     def __str__(self):
#         return f" {self.nombre} - {self.apellido} - {self.DNI} - {self.telefono} - {self.email}"


class Ficha_medica (models.Model):

    registro = models.IntegerField(unique=True)
    vacunas = models.CharField(max_length= 100, null=True, blank=True,)
    desparasitacion = models.CharField(max_length=50, null=True, blank=True,)
    castracion = models.CharField(max_length=50, null=True, blank=True,)
    observaciones = models.TextField(max_length=150,null=True, blank=True,)

    def __str__(self) -> str:
        return f" {self.registro} - {self.vacunas} - {self.desparacitacion} - {self.castracion} - {self.observaciones}"

  


class Refugio (models.Model):

    nombre = models.CharField(max_length= 50, unique=True)
    telefono = models.IntegerField(unique=True)
    email = models.EmailField(unique=True)
    direccion = models.TextField(max_length=100) 

    def __str__(self):
        return f" {self.nombre} - {self.telefono} - {self.email} - {self.direccion}"


# class Empleado (models.Model):

#     nombre = models.CharField(max_length= 50)
#     apellido = models.CharField(max_length= 50)
#     puesto = models.CharField(max_length= 50)
#     
#     def __str__(self):
#         return f" {self.nombre} - {self.apellido} - {self.puesto}"


# class Voluntario (models.Model):

#     puesto = models.CharField(max_length= 50)
#     observaciones = models.TextField(max_length=80,null=True, blank=True)
#     

#     def __str__(self):
#         return f" {self.puesto} - {self.observaciones}"

