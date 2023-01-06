from django.urls import path, include
from .views import *
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', paginaInicio, name="paginainicio"),
    path("registrousuario/", registroUsuario, name = "registrousuario"),
    path("ingresousuario/", ingresoUsuario, name = "ingresousuario" ),
    path("portal/", portal, name="portal"),
    path("postear/", agregarPosteo, name='postear'),
    path("verposteo/", verPosteo, name="verposteo"),
    path("editarposteo/<id>", editarPosteo, name="editarposteo"),
    path("eliminarposteo/<id>", eliminarPosteo, name="eliminarposteo"),
    path("verusuarios", verUsuarios, name = "verusuarios"),
    path("desconectarse/", LogoutView.as_view(next_page='paginainicio'), name='desconectarse'),#Funcion para desconectarse
    path("fotoPerfil/", fotoPerfil, name="fotoPerfil"), #Funcion para editar avatar
    path("perfil/<id>", perfil, name="perfil"),
    path("sobrenosotros/", sobreNosotros, name="sobrenosotros"),
    path("buscarposteo", buscar, name="buscarposteo"),
    path("editarusuario/<id>", editarUsuario, name="editarusuario"),
    path("paginaposteo/", paginaPosteo, name="paginaposteo"),
   #PATH PARA MENSAJERIA
    path("chat/", MandarMensajes, name="chat"),
    path("mensajeUsuarios", mensajeUsuarios , name = "mensajeUsuarios"),
    path("leerMensaje", leerMensaje , name = "leerMensaje"),
    path("enviadoMensaje", enviadoMensaje , name = "enviadoMensaje"),
    path("paginaposteo/<id>", paginaPosteo, name="paginaposteo"),
]


