#-------------- imports de funciones de django ----------
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

from datetime import datetime
#--------------- imports de forms creados en forms.py -----------
from AppUsuarios.forms import FormUsuario, PosteoForm, ImagenPerfilForm
#--------------- imports models creados en models.py ----------
from AppUsuarios.models import Posteo, ImagenPerfil
#--------------- imports de forms existentes en django ------------




#-------------------------------- PAGINA DE INICIO -------------------------------------------------------

def paginaInicio(request):
    return render(request, "Inicio.html")


#-------------------------------------- PORTAL/home ----------------------------------------

@login_required
def portal(request):
    return render(request, "Portal.html", {"imagen":mostrarImagen(request)})


#-------------------------------------------- USUARIOS ----------------------------------------

#---------- Registro usuario ------------------

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
@login_required
def verUsuarios(request):
    usuarios = User.objects.all()
    
    return render(request, 'VerUsuarios.html', {"usuarios": usuarios,"imagen":mostrarImagen(request)}) 
    

#----------- Inicio de sesion usuarios --------------

def ingresoUsuario(request):
    if request.method == "POST":
        form=AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            nombre_usuario = form.cleaned_data.get("username")
            clave_usuario = form.cleaned_data.get("password")
            usuario = authenticate (username=nombre_usuario, password=clave_usuario)
            if usuario is not None:
                login(request, usuario)
                return render(request, "Portal.html", {"mensaje": f"Hola {usuario}!", "imagen":mostrarImagen(request)})

            else:
                return render (request, "IngresoUsuario.html", {"form":form})
        else:
            return render (request, "IngresoUsuario.html",{"form":form})
    else:
        form=AuthenticationForm()
    
    return render (request, "IngresoUsuario.html",{"form":form})



#-------  FUNCION PARA AGREGAR IMAGEN ---------
@login_required
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
@login_required
def mostrarImagen(request):
    lista=ImagenPerfil.objects.filter(user=request.user)
    if len(lista)!=0:
        imagen=lista[0].imagen.url
    else:
        imagen="/media/Perfil/homero.jpg"
    return imagen






#------------------------------------------ POSTEOS ------------------------------------------------------------

#-----------------  Agregar Posteo -------------------
@login_required
def agregarPosteo(request):

    if request.method == "POST":
        form = PosteoForm(request.POST, request.FILES)
        if form.is_valid():

            datos=form.cleaned_data

            titulo_posteo=datos["titulo_posteo"]
            subtitulo_posteo=datos["subtitulo_posteo"]
            contenido_posteo=datos["contenido_posteo"]
            imagen_post=datos["imagen_post"]
            fecha_posteo_imagen_forms= datetime.now()
                      
            posteo1=Posteo( titulo_posteo=titulo_posteo,subtitulo_posteo=subtitulo_posteo,contenido_posteo=contenido_posteo, imagen_post=imagen_post, fecha_posteo_imagen=fecha_posteo_imagen_forms  ,usuario_posteo=request.user) 
            posteo1.save()

            return render(request, "Portal.html",{"imagen":mostrarImagen(request)})
        else:
            return render(request,"Postear.html", {"mensaje":"Formulario invalido","form":form,"imagen":mostrarImagen(request)})

    else:
        formulario = PosteoForm()

    return render(request, "Postear.html", {"form":formulario,"imagen":mostrarImagen(request)})


#------------------- Ver Posteo -------------------
@login_required
def verPosteo(request):

    posteos = Posteo.objects.all()
    datos= {"posteos":posteos}

    return render(request,"VerPosteos.html",{"posteos":posteos,"imagen":mostrarImagen(request)})


#----------------- Editar Posteo -------------------
@login_required
def editarPosteo(request,id):

    posteo=Posteo.objects.get(id=id)

    if request.method == "POST":
        formularioposteo = PosteoForm(request.POST, request.FILES, initial={"titulo_posteo":posteo.titulo_posteo,"subtitulo_posteo":posteo.subtitulo_posteo,"contenido_posteo":posteo.contenido_posteo,"imagen_post":posteo.imagen_post})

        if formularioposteo.is_valid():

            datos = formularioposteo.cleaned_data

                    
            posteo.imagen_post = datos["imagen_post"]
            posteo.titulo_posteo = datos["titulo_posteo"]
            posteo.subtitulo_posteo = datos["subtitulo_posteo"]
            posteo.contenido_posteo = datos["contenido_posteo"]
            posteo.fecha_posteo_imagen = datetime.now()

            posteo.save()

            return render(request,"VerPosteos.html", {"mensaje":"Posteo editado correctamente","imagen":mostrarImagen(request)}) #Cambiar redireccionamiento
        else: 
            print(formularioposteo.errors.as_data())
            formularioposteo = PosteoForm(initial={"titulo_posteo":posteo.titulo_posteo,"subtitulo_posteo":posteo.subtitulo_posteo,"contenido_posteo":posteo.contenido_posteo,"imagen_post":posteo.imagen_post})
            return render(request,"VerPosteos.html", {"mensaje":"Error en validacion de posteo", "formularioposteo":formularioposteo,"imagen":mostrarImagen(request)}) 
    else:
        formularioposteo=PosteoForm(initial={"titulo_posteo":posteo.titulo_posteo,"subtitulo_posteo":posteo.subtitulo_posteo,"contenido_posteo":posteo.contenido_posteo,"imagen_post":posteo.imagen_post})

    return render(request,"EditarPosteo.html", {"formularioposteo":formularioposteo,"posteo":posteo,"imagen":mostrarImagen(request)})


def editarUsuario(request,id):

    usuario = User.objects.get(id=id)
    
    if request.method=="POST":
        form=FormUsuario(request.POST)

        if form.is_valid():
            username=form.cleaned_data["username"]
            
            form.save()
            return render(request, "Perfil.html")
    else:
        form = FormUsuario(initial = {"nombre":usuario.username,"email":usuario.email})
    return render(request, 'EditarUsuario.html',{"form":form,"imagen":mostrarImagen(request)})

#---------------- Eliminar posteo ----------------
@login_required
def eliminarPosteo(request):

    if request.method == 'POST':
        id = request.POST['id']
        posteo = get_object_or_404(Posteo, pk=id)
        posteo.delete()
        return redirect('verposteo')

    return redirect('verposteo')



#--------------------------- PERFIL -------------------------------
@login_required
def perfil(request,id):

    perfil = User.objects.get(id=id)

    return render(request, "Perfil.html",{"imagen":mostrarImagen(request), "perfil":perfil})


#---------------------------- ABOUT US --------------------------------
@login_required
def sobreNosotros(request):
     return render(request, "SobreNosotros.html",{"imagen":mostrarImagen(request)})


#-------------------------- BUSCAR POSTEO ---------------------------------
@login_required
def buscar(request):
    if "titulo_posteo" in (request.GET):
        var1=request.GET ["titulo_posteo"]
        resultado=Posteo.objects.filter(titulo_posteo__icontains=var1)
        return render(request,"ResultadoBusqueda.html", {"resultado":resultado,"imagen":mostrarImagen(request)})
    else:
        return render(request, "VerPosteos.html")


def paginaPosteo(request,id):

    paginaposteo = Posteo.objects.get(id=id)

    return render(request, "PaginaPosteo.html",{"imagen":mostrarImagen(request), "paginaposteo":paginaposteo})



