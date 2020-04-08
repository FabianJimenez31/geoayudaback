from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser
from .models import iniciativa
from .serializers import IniciativaSerializer
# Create your views here.


class EntidadList(APIView):
    parser_classes = (JSONParser,)

    def get(self, request, tipo_iniciativa, format=None):
        iniciativa_object = iniciativa.objects.filter(tipo__nombre=tipo_iniciativa)
        serializer = IniciativaSerializer(many=True)
        return Response(serializer.data)