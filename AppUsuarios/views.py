from django.shortcuts import render
#-------------- imports de funciones de django ----------
from django.contrib.auth import login, authenticate, logout
#--------------- imports de forms creados en forms.py -----------
from AppUsuarios.forms import FormUsuario, FormEditarUsuario, PosteoForm
#--------------- imports de forms existentes en django ------------
from django.contrib.auth.forms import AuthenticationForm

from django.views.generic.list import ListView
from .models import Posteo
from django.contrib.auth.models import User




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

def portal(request, usuario):
    return render(request, "Portal.html", {"mensaje": f"bienvenido {usuario}"})

#------------- posteo ---------
class AgregarVistaPosteo(ListView):

    model = Posteo

    def get(self,request):
            form = PosteoForm()
            return render (request, "index.html", {"form":form})

    def post(self, request):
        form = PosteoForm(request.POST)
        if form.is_valid():
            datos = form.cleaned_data
            usuario_posteo2 = datos["usuario_posteo_forms"]
            titulo_posteo2 = datos["titulo_posteo_forms"]
            contenido_posteo2 = datos["contenido_posteo_forms"]
            imagen_posteo2 = datos["imagen_posteo_forms"]
            fecha_posteo_imagen2 = datos["fecha_posteo_imagen_forms"]

            objeto_usuario = User.objects.get(nombre = usuario_posteo2)
            objeto_posteo = Posteo.objects.create(usuario_posteo = objeto_usuario, titulo_posteo = titulo_posteo2 , contenido_posteo = contenido_posteo2, imagen_posteo = imagen_posteo2, fecha_posteo_imagen = fecha_posteo_imagen2)

            objeto_posteo.save()

            form = PosteoForm()

            return render(request, "otrotemplate.html", {form:"form"})
class TodosPosteos(AgregarVistaPosteo):
    models = Posteo

    def get (self,request):
        todos_posteos = self.model.objects.all().order_by("id")  
        return render(request, "TodosPosteos.html", {"posts":todos_posteos}) 
            