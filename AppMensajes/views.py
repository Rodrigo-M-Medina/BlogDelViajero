from django.shortcuts import render, get_object_or_404, redirect 
#get_object_or_404 Esta función llama al modelo dado y obtiene el objeto de eso, 
#si ese objeto o modelo no existe, genera la pagina error 404.
#redirect me sirve para redirigir la funcion al nombre que le doy en urls.py
from django.contrib.auth.decorators import login_required
from AppMensajes.forms import MensajeForm
from django.contrib.auth.models import User
from AppMensajes.models import *
from AppUsuarios.views import mostrarImagen


#----------------- MENSAJERIA ------------------------------------------
#------ mandar mensaje ------------ 
@login_required
def MandarMensajes(request): 
    if request.method == 'POST':
        form = MensajeForm(request.POST)
        if form.is_valid():
            mensaje = form.save(commit=False)
            mensaje.salida = request.user
            mensaje.save()
            return render(request, 'mandarMensajes.html', {'form': form,"imagen":mostrarImagen(request)})
    else:
        form = MensajeForm() 
    return render(request, 'mandarMensajes.html', {'form': form,"imagen":mostrarImagen(request)})

#------------- ver opciones de mensajes ----------------
@login_required
def mensajeUsuarios(request):
    return render(request, 'mensajeUsuarios.html',{'users': User.objects.exclude(username=request.user.username),"imagen":mostrarImagen(request)})


#------------- ver bandeja de mensajes y leerlos automaticamente ---------
@login_required 
def leerMensaje(request):
    usuario = request.user
    msj = Chat.objects.filter(entrada = usuario)
    for mensaje in msj:
        mensaje.leido = True
        mensaje.save()  
    return render(request, "leerMensaje.html", {"mensajes": msj,"imagen":mostrarImagen(request)})


#-------------- ver mensajes enviados y su estado ------------------
@login_required
def enviadoMensaje(request):
    usuario = request.user
    msj= Chat.objects.filter(salida = usuario)
    return render(request, "enviadoMensaje.html", {"mensajes": msj,"imagen":mostrarImagen(request)})

#------------- borrar mensajes creados -----------------
@login_required
def borrarMensaje(request):
    if request.method == 'POST':
        id = request.POST['id']
        mensaje = get_object_or_404(Chat, pk=id)
        mensaje.delete()
        return redirect('mensajeUsuarios')
    return redirect('mensajeUsuarios')
