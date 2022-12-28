from django.urls import path, include
from .views import *

urlpatterns = [
    path('', paginaInicio, name="paginainicio"),
    path ("registrousuario/", registroUsuario, name = "registrousuario"),
    path ("ingresousuario/", ingresoUsuario, name = "ingresousuario" ),
    path('desconectarse/', desconectarse, name="desconectarse"),
    path("postear/", agregarPosteo, name='postear'),
    
]