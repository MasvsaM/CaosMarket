from django.shortcuts import render

def index (request):
    comentario ={"titulo":"COMENTARIO ENVIADO DESDE DJANGO A LA PAGINA"}
    return render(request, "core/index.html", comentario)

def contactanos (request):
     return render(request, "core/contactanos.html")

def login (request):
     return render(request, "core/login.html")

def registro (request):

    return render(request, "core/registro.html")     

def ofertas (request):

    return render(request, "core/ofertas.html")   

def celulares (request):

    return render(request, "core/celulares_Apple.html")
def celularesAndroid (request):

    return render(request, "core/celulares_Android.html")
def celularesHauwei (request):

    return render(request, "core/celulares_Hauwei.html")

def computacionper (request):

    return render(request, "core/Computacion_Perifericos.html")
def computacioncomponentes (request):

    return render(request, "core/Computacion_Componentes.html")

def computaciongaming (request):

    return render(request, "core/Computacion_Gaming.html")





