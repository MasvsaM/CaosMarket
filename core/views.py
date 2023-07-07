from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages



def index(request):
    comentario = {"titulo": "COMENTARIO ENVIADO DESDE DJANGO A LA PAGINA"}
    return render(request, "core/index.html", comentario)


def contactanos(request):
    return render(request, "core/contactanos.html")


def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  # Redirige al usuario a la página deseada después del inicio de sesión exitoso
        else:
            messages.error(request, 'Credenciales inválidas. Por favor, inténtalo de nuevo.')
    return render(request, 'login.html')

def ofertas(request):
    return render(request, "core/ofertas.html")   

def celulares(request):
    return render(request, "core/celulares_Apple.html")

def celularesAndroid(request):
    return render(request, "core/celulares_Android.html")

def celularesHauwei(request):
    return render(request, "core/celulares_Hauwei.html")

def computacionper(request):
    return render(request, "core/Computacion_Perifericos.html")

def computacioncomponentes(request):
    return render(request, "core/Computacion_Componentes.html")

def computaciongaming(request):
    return render(request, "core/Computacion_Gaming.html")


def registro(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        user = User.objects.create_user(username=username, password=password, email=email)
        user.save()
        return redirect('login')
    else:
        return render(request, 'core/registro.html')

