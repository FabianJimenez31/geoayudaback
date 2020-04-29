from .models import (
                    Departamento,
                    Ciudad,
                    fase_inicitiva,
                    nivel_apoyo,
                    tipo_iniciativa,
                    poblacion,
                    entidad,
                    sector,
                    iniciativa
                    
                    )
from rest_framework import serializers


class DepartamentoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Departamento
        fields = ('id', 'nombre')


class CiudadSerializer(serializers.ModelSerializer):
    departamento = DepartamentoSerializer(read_only=True)
    class Meta:
        model = Ciudad
        fields = ('id', 'nombre', 'departamento')

class FaseIinicativaSerializer(serializers.ModelSerializer):

    class Meta:
        model = fase_inicitiva
        fields = ('id', 'nombre')
    
class NivelApoyoSerializer(serializers.ModelSerializer):

    class Meta:
        model = nivel_apoyo
        fields = ('id', 'nombre')

class TipoIiniciativaSerializer(serializers.ModelSerializer):

    class Meta:
        model = tipo_iniciativa
        fields = ('id', 'nombre')

class PoblacionSerializer(serializers.ModelSerializer):

    class Meta:
        model = poblacion
        fields = ('id', 'nombre', 'descripcion', 'vulnerable')

class EntidadSerializer(serializers.ModelSerializer):

    class Meta:
        model = entidad
        fields = ('id', 'nombre', 'direccion')


class SectorSerializer(serializers.ModelSerializer):

    class Meta:
        model = sector
        fields = ('id','nombre')


class IniciativaSerializer(serializers.ModelSerializer):
    fase = FaseIinicativaSerializer(read_only=True)
    nivel_apoyo = NivelApoyoSerializer(read_only=True)
    tipo = TipoIiniciativaSerializer(read_only=True)
    entidad = EntidadSerializer(read_only=True)
    sector = SectorSerializer(read_only=True)
    ciudad = CiudadSerializer(read_only=True)
    poblacion = PoblacionSerializer(read_only=True)

    class Meta:
        model = iniciativa
        fields = (
            'id',
	    'nombre',
 	    'descripcion', 
            'poblacion_estimada', 
            'direccion',
            'url',
            'latitud',
            'longitud',
            'fase',
            'nivel_apoyo',
            'tipo',
            'entidad',
            'sector',
            'ciudad',
            'poblacion'
             )