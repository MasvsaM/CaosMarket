from rest_framework import generics
from .models import Producto, Sucursal
from .serializers import ProductoSerializer, SucursalSerializer

class ProductoList(generics.ListCreateAPIView):
    serializer_class = ProductoSerializer


    def get_queryset(self):
        queryset = Producto.objects.all()
        Sucursal = self.request.query_params.get('Sucursal')
        if Sucursal is not None:
            queryset = queryset.filter(ciudadproducto=Sucursal)
        return queryset
    

class ProductoDetail(generics.RetrieveUpdateDestroyAPIView):
        serializer_class = ProductoSerializer
        queryset = Producto.objects.all()


class SucursalDetail(generics.ListCreateAPIView):
     serializer_class = SucursalSerializer
     queryset = Sucursal.objects.all()
     

class SucursalLista(generics.RetrieveUpdateDestroyAPIView):
     serializer_class = SucursalSerializer
     
     queryset = Sucursal.objects.all()
    
  
     


