from django.shortcuts import render
#-------------- imports de funciones de django ----------
from django.contrib.auth import login, authenticate, logout
#--------------- imports de forms creados en forms.py -----------
from AppUsuarios.forms import FormUsuario, FormEditarUsuario
#--------------- imports de forms existentes en django ------------
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
#--------------- import de AppPosteos ------------
from AppPosteos.views import portal


#----------- Pagina de inicio ----------------

def paginaInicio(request):
    return render(request, "Inicio.html")


#---------- registro usuario ------------------

def registroUsuario(request):
    if request.method=="POST":
        form=FormUsuario(request.POST)
        if form.is_valid():
            username=form.cleaned_data["username"]
            form.save()
            return render(request, "Inicio.html")
    else:
        form = FormUsuario()
    return render(request, 'RegistroUsuario.html',{"form":form})



#----------- inicio de sesion --------------

def ingresoUsuario(request):
    if request.method == "POST":
        form=AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            nombre_usuario = form.cleaned_data.get("username")
            clave_usuario = form.cleaned_data.get("password")
            usuario = authenticate (username=nombre_usuario, password=clave_usuario)
            if usuario is not None:
                login(request, usuario)
                return portal(request, usuario)

            else:
                return render (request, "IngresoUsuario.html", {"form":form})
        else:
            return render (request, "IngresoUsuario.html",{"form":form})
    else:
        form=AuthenticationForm()
    
    return render (request, "IngresoUsuario.html",{"form":form})

#-------- desconectar sesiòn ----------

def desconectarse(request):
    logout(request)
    return render(request, "Inicio.html", {"mensaje":"Te desconectaste"})
