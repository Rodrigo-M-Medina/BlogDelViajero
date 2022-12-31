from django.urls import path, include
from .views import *
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

urlpatterns = [
    path('', paginaInicio, name="paginainicio"),
    path ("registrousuario/", registroUsuario, name = "registrousuario"),
    path ("ingresousuario/", ingresoUsuario, name = "ingresousuario" ),
    path('desconectarse/', desconectarse, name="desconectarse"),
    path("postear/", agregarPosteo, name='postear'),
    path("verposteo/", verPosteo, name="verposteo"),
    path("editarposteo/<id>", editarPosteo, name="editarposteo"),
    path("portal/", portal, name="portal1"),
    path("fotoPerfil/", fotoPerfil, name="fotoPerfil"),
    path("eliminarposteo/<id>", eliminarPosteo, name="eliminarposteo"),
    path("verusuarios", verUsuarios, name = "verusuarios"),
]

