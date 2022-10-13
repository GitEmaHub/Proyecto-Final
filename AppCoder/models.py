from django.db import models

# Create your models here.


class About(models.Model):
    
    trabajo = models.CharField(max_length=60)
    fecha = models.CharField(max_length=60)


class LatestWork(models.Model):

    trabajo = models.CharField(max_length=60)
    fecha = models.CharField(max_length=60)


class Comunidad(models.Model):
    
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)


class Contacto(models.Model):
    
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    correo = models.EmailField()
    telefono = models.IntegerField()
    motivo = models.CharField(max_length=200)
    