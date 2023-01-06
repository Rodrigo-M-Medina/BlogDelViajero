from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from AppMensajes.forms import MensajeForm
from django.contrib.auth.models import User
from AppMensajes.models import *

#----------------- MENSAJERIA -------------------------- INCOMPLETA
@login_required
def MandarMensajes(request):#por ahora solo puedo mandar mensajes desde un opcion de mensajes 
    if request.method == 'POST':
        form = MensajeForm(request.POST)
        if form.is_valid():
            # Guardando mensaje en la base de datos
            mensaje = form.save(commit=False)#commit false? se supone que es un booleano que me deja ver el mensaje antes de guardar
            mensaje.salida = request.user
            mensaje.save()
            return render(request, 'mandarMensajes.html', {'form': form})
    else:
        form = MensajeForm() 
    return render(request, 'mandarMensajes.html', {'form': form})

@login_required
def mensajeUsuarios(request):
    return render(request, 'mensajeUsuarios.html',{'users': User.objects.exclude(username=request.user.username)})

@login_required 
def leerMensaje(request):
    usuario = request.user
    msj = Chat.objects.filter(entrada = usuario)
    for mensaje in msj:
        mensaje.leido = True
        mensaje.save()  
    return render(request, "leerMensaje.html", {"mensajes": msj,})

@login_required
def enviadoMensaje(request):
    usuario = request.user
    msj= Chat.objects.filter(salida = usuario)
    return render(request, "enviadoMensaje.html", {"mensajes": msj})

