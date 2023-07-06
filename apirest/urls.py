from django.urls import path
from .views import ProductoList, ProductoDetail, SucursalDetail, SucursalLista,Logout,registrouser



urlpatterns=[


    path('Producto/', ProductoList.as_view(),name = 'Producto'),
    path('Producto/<int:pk>/', ProductoDetail.as_view()),
    path('Sucursal/<int:pk>', SucursalLista.as_view()),
    path('Sucursal/', SucursalDetail.as_view()),
    path('registrouser/', registrouser, name='registrouser'),
   


    ]