from django.urls import path
from .views import *


urlpatterns = [
    #PATH PARA MENSAJERIA
    path("chat/", MandarMensajes, name="chat"),
    path("mensajeUsuarios", mensajeUsuarios , name = "mensajeUsuarios"),
    path("leerMensaje", leerMensaje , name = "leerMensaje"),
    path("enviadoMensaje", enviadoMensaje , name = "enviadoMensaje"),
    path('borrarmsj/', borrarMensaje, name='borrarMensaje'),
]

