from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    #path de inicio
    path("portal/", portal, name="portal"),
    path('', paginaInicio, name="paginainicio"),
    path("registrousuario/", registroUsuario, name = "registrousuario"),
    path("ingresousuario/", ingresoUsuario, name = "ingresousuario" ),

    #path de posteos
    path("postear/", agregarPosteo, name='postear'),
    path("verposteo/", verPosteo, name="verposteo"),
    path("editarposteo/<id>", editarPosteo, name="editarposteo"),
    path("eliminarposteo/", eliminarPosteo, name="eliminarposteo"),
    path("buscarposteo", buscar, name="buscarposteo"),
    path("paginaposteo/<id>", paginaPosteo, name="paginaposteo"),

    #path usuarios
    path("verusuarios", verUsuarios, name = "verusuarios"),
    path("fotoPerfil/", fotoPerfil, name="fotoPerfil"), #Funcion para editar avatar
    path("perfil/", perfil, name="perfil"),
    path("editarusuario/", editarUsuario, name="editarusuario"),
    path("agregarbiografia", agregarBiografia, name="agregarbiografia"),
    path('perfilU/<str:username>/', perfilUsuario, name="perfilusuario"),


    #path extras
    path("sobrenosotros/", sobreNosotros, name="sobrenosotros"),
    path("desconectarse/", LogoutView.as_view(next_page='paginainicio'), name='desconectarse'),#Funcion para desconectarse 
]


#reciben la vista creada en AppUsuarios para generar paginas de fallos
handler404 = custom_404
handler500 = custom_500
