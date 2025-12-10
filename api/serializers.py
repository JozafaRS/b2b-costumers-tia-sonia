from rest_framework import serializers
from api.models import *

class VendedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendedor
        fields = "__all__"

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = "__all__"

class ParametroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parametro
        fields = "__all__"