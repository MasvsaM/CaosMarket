from django.urls import path, include
from .views import index, login, registro, contactanos, ofertas, celulares, computacionper, celularesAndroid, celularesHauwei, computacioncomponentes, computaciongaming
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from . import views

urlpatterns=[
    path('',index, name="index"),
    path('registro/',registro, name="registro"),
    path('login/',LoginView.as_view(template_name="core/login.html"), name="login"),
    path('logout/',LogoutView.as_view(template_name="core/index.html"), name="logout"),
    path('contactanos/',contactanos, name="contactanos"),
    path('carrito/', views.carrito, name='carrito'),
    path('ofertas/',ofertas, name="ofertas"),
    path('celulares/',celulares, name="celulares"),
    path('celularesAndroid/',celularesAndroid, name="celularesAndroid"),
    path('celularesHauwei/',celularesHauwei, name="celularesHauwei"),
    path('computacionperifericos/',computacionper, name="computacionperifericos"),
    path('computacioncomponentes/',computacioncomponentes, name="computacioncomponentes"),
    path('computaciongaming/',computaciongaming, name="computaciongaming"),
    path('apirest/', include('apirest.urls')),
    path('admin/', admin.site.urls),
    path('indexadmin/', index, name='indexadmin'),
    
    

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


