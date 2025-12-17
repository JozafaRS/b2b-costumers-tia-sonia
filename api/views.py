from rest_framework import generics, viewsets
from api.models import Vendedor, Cliente, Parametro
from api.serializers import VendedorSerializer, ClienteSerializer, ParametroSerializer

class VendedorViewSet(viewsets.ModelViewSet):
    queryset = Vendedor.objects.all().filter(ativo=True)
    serializer_class = VendedorSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class ParametroViewSet(viewsets.ModelViewSet):
    queryset = Parametro.objects.all()
    serializer_class = ParametroSerializer