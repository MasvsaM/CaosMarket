from django.urls import path
from .views import ProductoList, ProductoDetail, SucursalDetail, SucursalLista

app_name = 'apirest' 

urlpatterns = [
    path('Producto/', ProductoList.as_view(), name='producto_list'),
    path('Producto/<int:pk>/', ProductoDetail.as_view(), name='producto_detail'),
    path('Sucursal/', SucursalLista.as_view(), name='sucursal_list'),
    path('Sucursal/<int:pk>/', SucursalDetail.as_view(), name='sucursal_detail'),
]
