from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import *


urlpatterns = [
    #PATH PARA MENSAJERIA
    path("chat/", MandarMensajes, name="chat"),
    path("mensajeUsuarios", mensajeUsuarios , name = "mensajeUsuarios"),
    path("leerMensaje", leerMensaje , name = "leerMensaje"),
    path("enviadoMensaje", enviadoMensaje , name = "enviadoMensaje"),
    
]