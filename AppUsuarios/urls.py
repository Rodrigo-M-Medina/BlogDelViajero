from django.urls import path, include
from .views import *


urlpatterns = [
    path('', paginaInicio, name="paginainicio"),
    path ("registrousuario/", registroUsuario, name = "registrousuario"),
    path ("ingresousuario/", ingresoUsuario, name = "ingresousuario" ),
    path('desconectarse/', desconectarse, name="desconectarse"),
    path("todos_posteos/", TodosPosteos.as_view() ,name='todosposteos'),
    path("postear/", AgregarVistaPosteo.as_view(), name='postear'),
    
]