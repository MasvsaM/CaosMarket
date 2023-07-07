from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
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
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  # Redirige al usuario a la página deseada después del inicio de sesión exitoso
        else:
            messages.error(request, 'Credenciales inválidas. Por favor, inténtalo de nuevo.')
    return render(request, 'core/login.html')

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = User.objects.get(email=email)
            user.set_password(password)
            user.save()
            user = authenticate(request, username=email, password=password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'core/registro.html', {'form': form})

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

def carrito(request):
    return render(request, 'core/carrito.html')
