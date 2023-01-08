from django.urls import path
from AppUsuarios.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', paginaInicio, name="paginainicio"),
    path("registrousuario/", registroUsuario, name = "registrousuario"),
    path("ingresousuario/", ingresoUsuario, name = "ingresousuario" ),
    path("desconectarse/", LogoutView.as_view(next_page='paginainicio'), name='desconectarse'),#Funcion para desconectarse
    path("portal/", portal, name="portal"),
    path("sobrenosotros/", sobreNosotros, name="sobrenosotros"),

    path("postear/", agregarPosteo, name='postear'),
    path("verposteo/", verPosteo, name="verposteo"),
    path("editarposteo/<id>", editarPosteo, name="editarposteo"),
    path("eliminarposteo/", eliminarPosteo, name="eliminarposteo"),
    path("paginaposteo/<id>", paginaPosteo, name="paginaposteo"),
    path("buscarposteo", buscar, name="buscarposteo"),
    
    path("fotoPerfil/", fotoPerfil, name="fotoPerfil"),
    path("perfil/", perfil, name="perfil"),
    path("editarusuario/", editarUsuario, name="editarusuario"),
    path("verusuarios", verUsuarios, name = "verusuarios"),
]


handler404 = custom_404
handler500 = custom_500
