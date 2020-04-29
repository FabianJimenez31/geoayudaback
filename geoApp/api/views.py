from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser
from drf_yasg.utils import swagger_auto_schema 
from drf_yasg import openapi
from .models import iniciativa,Departamento,Ciudad
from .serializers import IniciativaSerializer,DepartamentoSerializer,CiudadSerializer
# Create your views here.


class EntidadList(APIView):
    parser_classes = (JSONParser,)

    @swagger_auto_schema(
        responses={200:openapi.Response('Iniciativa',IniciativaSerializer)},
        tags=['Store']
    )
    def get(self, request, tipo_iniciativa, format=None):
        iniciativa_object = iniciativa.objects.filter(tipo__nombre=tipo_iniciativa)
        serializer = IniciativaSerializer(iniciativa_object ,many=True)
        return Response(serializer.data)

# Get list of available departments

class DepartamentosList(APIView):
    parser_classes = (JSONParser,)

    @swagger_auto_schema(
        reponses={200:openapi.Response('Departamentos',DepartamentoSerializer)},
    )

    def get(self, request, format=None):
        departamentos = Departamento.objects.all()
        serializer = DepartamentoSerializer(departamentos ,many=True)
        return Response(serializer.data)

# Get list of available cities

class CiudadesList(APIView):
    parser_classes = (JSONParser,)

    @swagger_auto_schema(
        reponses={200:openapi.Response('Ciudades',CiudadSerializer)},
    )

    def get(self, request, format=None):
        ciudades = Ciudad.objects.all()
        serializer = CiudadSerializer(ciudades ,many=True)
        return Response(serializer.data)


# Get list of available initiatives by department

class CiudadesByDepartment(APIView):
    parser_classes = (JSONParser,)

    @swagger_auto_schema(
        reponses={200:openapi.Response('Ciudades',CiudadSerializer)},
    )

    def get(self, request, departamento_id, format=None):
        ciudades = Ciudad.objects.filter(departamento=departamento_id)
        serializer = CiudadSerializer(ciudades ,many=True)
        return Response(serializer.data)






class Iniciativas(APIView):
    parser_classes = (JSONParser,)

    @swagger_auto_schema(
        responses={200:openapi.Response('Iniciativa',IniciativaSerializer)},
        tags=['Iniciativa']
    )
    def get(self, request, format=None):
        ciudades = iniciativa.objects.all()
        serializer = IniciativaSerializer(ciudades ,many=True)
        return Response(serializer.data)



# Get list of available initiatives by city
class IniciativasByCiudad(APIView):
    parser_classes = (JSONParser,)

    @swagger_auto_schema(
        reponses={200:openapi.Response('Iniciativas',IniciativaSerializer)},
    )

    def get(self, request, ciudad_id, format=None):
        ciudades = iniciativa.objects.filter(ciudad=ciudad_id)
        serializer = IniciativaSerializer(ciudades ,many=True)
        return Response(serializer.data)