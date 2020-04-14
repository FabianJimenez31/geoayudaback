from django.db import models

# Create your models here.

class tipo_entidad(models.Model):
    nombre = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nombre

class tipo_poblacion(models.Model):
    nombre = models.CharField(max_length=200)
    def __str__(self):
        return self.nombre

class tipo_iniciativa(models.Model):
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

class fase_inicitiva(models.Model):
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

class nivel_apoyo(models.Model):
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

class poblacion(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200)
    vulnerable = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre

class sector(models.Model):
    nombre = models.CharField(max_length=200)
    def __str__(self):
        return self.nombre

class Departamento(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

class Ciudad(models.Model):
    nombre = models.CharField(max_length=255)
    departamento = models.ForeignKey(Departamento,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre


class iniciativa(models.Model):
    fase = models.ForeignKey(fase_inicitiva, on_delete=models.CASCADE)
    nivel_apoyo = models.ForeignKey(nivel_apoyo, on_delete=models.CASCADE)
    tipo = models.ForeignKey(tipo_iniciativa, on_delete = models.CASCADE)
    poblacion = models.ForeignKey(poblacion, on_delete = models.CASCADE)
    entidad = models.ForeignKey('entidad', on_delete = models.CASCADE)
    sector = models.ForeignKey(sector, on_delete = models.CASCADE)
    poblacion_estimada = models.IntegerField()
    direccion =  models.CharField(max_length=200)
    url = models.TextField(null=True)
    ciudad = models.ForeignKey(Ciudad, on_delete = models.CASCADE)
    latitud = models.FloatField()
    longitud = models.FloatField()
    nombre = models.TextField(null=True)
    descripcion = models.TextField(null=True)
    link_image = models.TextField(null=True)

class entidad(models.Model):
    nombre =  models.CharField(max_length=200)
    direccion =  models.CharField(max_length=200)
    tipo = models.ForeignKey(tipo_entidad, on_delete=models.CASCADE)