from django.db import models


# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    activo = models.BooleanField(default=True)



    # Modelo de usuarios


    # Nueva funcionalidad