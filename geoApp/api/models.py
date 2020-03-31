from django.db import models

# Create your models here.

class tipo_entidad(models.Model):
    nombre = models.CharField(max_length=200)

class tipo_poblacion(models.Model):
    nombre = models.CharField(max_length=200)

class tipo_iniciativa(models.Model):
    nombre = models.CharField(max_length=200)

class fase_inicitiva(models.Model):
    nombre = models.CharField(max_length=200)

class nivel_apoyo(models.Model):
    nombre = models.CharField(max_length=200)

class poblacion(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200)

class iniciativa(models.Model):
    fase = models.ForeignKey(fase_inicitiva, on_delete=models.CASCADE)
    apoyo = models.ForeignKey(nivel_apoyo, on_delete=models.CASCADE)
    tipo = models.ForeignKey(tipo_iniciativa, on_delete = models.CASCADE)
    poblacion = models.ForeignKey(poblacion, on_delete = models.CASCADE)
    entidad = models.ForeignKey('entidad', on_delete = models.CASCADE)

class entidad(models.Model):
    nombre =  models.CharField(max_length=200)
    dirección =  models.CharField(max_length=200)
    tipo = models.ForeignKey(tipo_entidad, on_delete=models.CASCADE)
    latitud = models.FloatField()
    longitud = models.FloatField()