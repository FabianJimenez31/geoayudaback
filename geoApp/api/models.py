from django.db import models

# Create your models here.

class fase_inicitiva(models.Model):
    nombre = models.CharField(max_length=200)

class nivel_apoyo(models.Model):
    nombre = models.CharField(max_length=200)

class iniciativa(models.Model):
    sector = models.CharField(max_length=200)
    fase = models.ForeignKey(fase_inicitiva, on_delete=models.CASCADE)
    apoyo = models.ForeignKey(nivel_apoyo, on_delete=models.CASCADE)
    latitud = models.FloatField()
    longitud = models.FloatField()

class entidad(models.Model):
    nombre =  models.CharField(max_length=200)
    dirección =  models.CharField(max_length=200)
    