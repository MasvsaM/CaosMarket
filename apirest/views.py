from rest_framework import generics
from .models import Producto, Sucursal
from .serializers import ProductoSerializer, SucursalSerializer

from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import FormView
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import redirect,render
from django.contrib.auth.models import User

class ProductoList(generics.ListCreateAPIView):
    serializer_class = ProductoSerializer


    def get_queryset(self):
        queryset = Producto.objects.all()
        Sucursal = self.request.query_params.get('Sucursal')
        if Sucursal is not None:
            queryset = queryset.filter(ciudadproducto=Sucursal)
        return queryset
    permission_classes = (IsAuthenticated,)
    authentication_class = (TokenAuthentication)

class ProductoDetail(generics.RetrieveUpdateDestroyAPIView):
        serializer_class = ProductoSerializer
        queryset = Producto.objects.all()


class SucursalDetail(generics.ListCreateAPIView):
     serializer_class = SucursalSerializer
     queryset = Sucursal.objects.all()
     

class SucursalLista(generics.RetrieveUpdateDestroyAPIView):
     serializer_class = SucursalSerializer
     
     queryset = Sucursal.objects.all()
    
  
     

class Login(FormView):
     template_name= "login.html"
     form_class = AuthenticationForm
     success_url = reverse_lazy('Producto')


@method_decorator(csrf_protect)
@method_decorator(never_cache)

def dispatch(self,request,*args,**kwargs):
     if request.user.is_authenticated:
          return HttpResponseRedirect(self.get_success_url())
     else:
          return super(login,self).dispatch(request,*args,**kwargs)
     
def form_valid(self,form):
    user = authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password'])
    token,_ = Token.objects.get_or_create(user = user)
    if token:
         login(self.request, form.get_user())
         return super(Login,self).form_valid(form)

def Logout(request):
     def get(self,request, format = None):
          username = username(request)
          if username != None:
               logout(request)
          return redirect('index')
     
def registrouser(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        User.objects.create_superuser(username=username, email=email, password=password)



        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('index')
    
    return render(request, 'registro.html')
     
     