from django.shortcuts import render, redirect
#-------------- imports de funciones de django ----------
from django.contrib.auth import login, authenticate, logout
#--------------- imports de forms creados en forms.py -----------
from AppUsuarios.forms import FormUsuario, FormEditarUsuario, PosteoForm, ImagenPerfilForm
#--------------- imports de forms existentes en django ------------
from django.contrib.auth.forms import AuthenticationForm

from AppUsuarios.models import Posteo, ImagenPerfil

from django.contrib.auth.models import User

from datetime import datetime




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


#---------- Ver usuarios ------------------

def verUsuarios(request):
    usuarios = User.objects.all()
    
    return render(request, 'VerUsuarios.html', {"usuarios": usuarios}) 
    



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
                return render(request, "Portal.html", {"mensaje": f"bienvenido{usuario}", "imagen":mostrarImagen(request)})

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
    return render(request, "Portal.html", {"mensaje": f"bienvenido {usuario}", "imagen":mostrarImagen(request)})

#-----------------  Agregar Posteo
def agregarPosteo(request):

    if request.method == "POST":
        form = PosteoForm(request.POST, request.FILES)
        if form.is_valid():
            datos=form.cleaned_data

            titulo_posteo=datos["titulo_posteo"]
            contenido_posteo=datos["contenido_posteo"]
            imagen_post=datos["imagen_post"]
            fecha_posteo_imagen_forms= datetime.now()
                      
            posteo1=Posteo( titulo_posteo=titulo_posteo,contenido_posteo=contenido_posteo, imagen_post=imagen_post, fecha_posteo_imagen=fecha_posteo_imagen_forms  ,usuario_posteo=request.user) 
            posteo1.save()

            return render(request, "Portal.html" )
        else:
            return render(request,"Postear.html", {"mensaje":"Formulario invalido","form":form})

    else:
        formulario = PosteoForm()

    return render(request, "Postear.html", {"form":formulario})

#----------- Ver Posteo -------------
def verPosteo(request):

    posteos = Posteo.objects.all()

    datos= {"posteos":posteos}

    return render(request,"VerPosteos.html",datos)


#-------------Editar Posteo -------------
def editarPosteo(request,id):

    posteo=Posteo.objects.get(id=id)

    if request.method == "POST":
        formularioposteo = PosteoForm(request.POST, request.FILES)

        if formularioposteo.is_valid():
            datos = formularioposteo.cleaned_data 
            posteo.titulo_posteo = datos["titulo_posteo"]
            posteo.contenido_posteo = datos["contenido_posteo"]
            posteo.imagen_post = datos["imagen_post"]
            posteo.fecha_posteo_imagen = datetime.now()

            posteo.save()

            return render(request,"Portal.html", {"mensaje":"Posteo editado correctamente"})
        else: 
            return render(request,"VerPosteos.html", {"mensaje":"Error en validacion de posteo"})
    else:
        formularioposteo=PosteoForm(initial={"titulo_posteo":posteo.titulo_posteo,"contenido_posteo":posteo.contenido_posteo,"imagen_post":posteo.imagen_post})

        return render(request,"EditarPosteo.html", {"formularioposteo":formularioposteo,"posteo":posteo})


#----------eliminar posteo -----------
def eliminarPosteo(request, id):
        posteo = Posteo.objects.get(id = id)
        posteo.delete()
        posteo = Posteo.objects.all()  
 
        posteo = {"posteos": posteo}
 
        return render(request, "VerPosteos.html", posteo)

#-------  FUNCION PARA AGREGAR IMAGEN ---------

def fotoPerfil(request):
    if request.method=="POST":
        form=ImagenPerfilForm(request.POST, request.FILES)
        if form.is_valid():
            imagenXdefecto=ImagenPerfil.objects.filter(user=request.user)
            if len(imagenXdefecto)!=0:
                imagenXdefecto[0].delete()
            imagen=ImagenPerfil(user=request.user, imagen=request.FILES["imagen"])
            imagen.save()
            return render(request, "Portal.html", {"imagen":mostrarImagen(request)})
        else:
            return render(request, "agregarImagen.html", {"formulario": form, "usuario": request.user, "imagen":mostrarImagen(request)})
    else:
        form=ImagenPerfilForm()
        return render(request , "agregarImagen.html", {"formulario": form, "usuario": request.user, "imagen":mostrarImagen(request)})

#--------- FUNCION PARA TRAER LA IMAGEN -----------------

def mostrarImagen(request):
    lista=ImagenPerfil.objects.filter(user=request.user)
    if len(lista)!=0:
        imagen=lista[0].imagen.url
    else:
        imagen="/media/Perfil/homero.jpg"
    return imagen

