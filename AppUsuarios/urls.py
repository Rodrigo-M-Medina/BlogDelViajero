from django.urls import path, include
from AppUsuarios.views import *


urlpatterns = [
    path('', paginaInicio, name="paginainicio"),
    path ("registrousuario/", registroUsuario, name = "registrousuario"),
    path ("ingresousuario/", ingresoUsuario, name = "ingresousuario" ),
    path('desconectarse/', desconectarse, name="desconectarse"),
    
]