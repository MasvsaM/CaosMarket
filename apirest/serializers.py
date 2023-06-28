from rest_framework import serializers
from .models import Producto, Sucursal

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ('__all__')



class SucursalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sucursal
        fields = ('__all__')