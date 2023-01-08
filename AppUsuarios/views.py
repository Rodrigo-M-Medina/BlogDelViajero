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


#-------- Funciones para las paginas de error ----------------
def custom_404(request, exception):
    return render(request, '404.html', {}, status=404)

def custom_500(request):
    return render(request, '500.html', {}, status=500)




#--------------------------------------- PAGINAS DE INICIO ---------------------------------------------
def paginaInicio(request):
    return render(request, "Inicio.html")
#------- PORTAL/home ------------
@login_required
def portal(request):
    return render(request, "Portal.html", {"imagen":mostrarImagen(request)})
#---------------- ABOUT US --------
@login_required
def sobreNosotros(request):
     return render(request, "SobreNosotros.html",{"imagen":mostrarImagen(request)})
#---------------------------------------------------- USUARIOS -----------------------------------------------

#---------- Registro usuario ------------------
def registroUsuario(request):
    if request.method=="POST":
        form=FormUsuario(request.POST)
        if form.is_valid():
            username=form.cleaned_data["username"]
            form.save()
            user = authenticate(username=form.cleaned_data["username"],password=form.cleaned_data["password1"])
            login(request, user)
            return render(request, "Portal.html",{"imagen":mostrarImagen(request)})
    else:
        form = FormUsuario()
    return render(request, 'RegistroUsuario.html',{"form":form})

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

#-------------- Editar usuario ----------------

def editarUsuario(request):
    if request.user.is_authenticated or request.user.is_superuser:
        usuario = request.user
        form=FormUsuario(request.POST, instance=request.user)
        if form.is_valid():
            if 'username' in request.POST:
                usuario.username = form.cleaned_data['username']
            if 'email' in request.POST:
                usuario.email = form.cleaned_data['email']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            if password1 and password2 and password1 == password2:
                usuario.set_password(password1)
            usuario.save()
            return render(request, "Perfil.html",{"imagen":mostrarImagen(request),"perfil":usuario})

        else:
            form = FormUsuario(initial = {"username":usuario.username,"email":usuario.email})
            return render(request, 'EditarUsuario.html',{"form":form,"imagen":mostrarImagen(request)})
    return render(request, "Perfil.html", {"imagen":mostrarImagen(request)})

#---------- Ver usuarios ------------------
@login_required
def verUsuarios(request):
    if request.user.is_superuser:
        usuarios = User.objects.all()
        return render(request, 'VerUsuarios.html', {"usuarios": usuarios,"imagen":mostrarImagen(request)}) 
    else:
     return redirect("portal")


#----------------------- PERFIL -------------------------------
@login_required
def perfil(request):

    perfil = request.user

    return render(request, "Perfil.html",{"imagen":mostrarImagen(request), "perfil":perfil})


#-------  FUNCION PARA AGREGAR AVATAR ---------
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
            subtitulo2_posteo=datos["subtitulo2_posteo"]
            contenido_posteo=datos["contenido_posteo"]
            imagen_post=datos["imagen_post"]
            fecha_posteo_imagen_forms= datetime.now()
                      
            posteo1=Posteo( titulo_posteo=titulo_posteo,subtitulo_posteo=subtitulo_posteo,subtitulo2_posteo=subtitulo2_posteo,contenido_posteo=contenido_posteo, imagen_post=imagen_post, fecha_posteo_imagen=fecha_posteo_imagen_forms  ,usuario_posteo=request.user) 
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

    return render(request,"VerPosteos.html",{"posteos":posteos,"imagen":mostrarImagen(request)})


#----------------- Editar Posteo -------------------
@login_required
def editarPosteo(request,id):

    posteo=Posteo.objects.get(id=id)
    
    if not (request.user.is_superuser or request.user == posteo.usuario_posteo):
        # si el usuario no es el superuser o el usuario que creo el posteo te redirige a ver posteos
        return render(request,"VerPosteos.html", {"mensaje":"No estas autorizado para editar el posteo","imagen":mostrarImagen(request)}) 
    else:
        if request.method == "POST":
            formularioposteo = PosteoForm(request.POST, request.FILES, initial={"titulo_posteo":posteo.titulo_posteo,"subtitulo_posteo":posteo.subtitulo_posteo,"subtitulo2_posteo":posteo.subtitulo2_posteo,"contenido_posteo":posteo.contenido_posteo,"imagen_post":posteo.imagen_post})

            if formularioposteo.is_valid():

                datos = formularioposteo.cleaned_data
                   
                posteo.imagen_post = datos["imagen_post"]
                posteo.titulo_posteo = datos["titulo_posteo"]
                posteo.subtitulo_posteo = datos["subtitulo_posteo"]
                posteo.subtitulo2_posteo= datos ["subtitulo2_posteo"]
                posteo.contenido_posteo = datos["contenido_posteo"]
                posteo.fecha_posteo_imagen = datetime.now()

                posteo.save()

                return render(request,"VerPosteos.html", {"mensaje":"Posteo editado correctamente","imagen":mostrarImagen(request)}) 
            else: 
                print(formularioposteo.errors.as_data())
                formularioposteo = PosteoForm(initial={"titulo_posteo":posteo.titulo_posteo,"subtitulo_posteo":posteo.subtitulo_posteo,"subtitulo2_posteo":posteo.subtitulo2_posteo,"contenido_posteo":posteo.contenido_posteo,"imagen_post":posteo.imagen_post})
                return render(request,"VerPosteos.html", {"mensaje":"Error en validacion de posteo", "formularioposteo":formularioposteo,"imagen":mostrarImagen(request)}) 
        else:
            formularioposteo=PosteoForm(initial={"titulo_posteo":posteo.titulo_posteo,"subtitulo_posteo":posteo.subtitulo_posteo,"subtitulo2_posteo":posteo.subtitulo2_posteo,"contenido_posteo":posteo.contenido_posteo,"imagen_post":posteo.imagen_post})

            return render(request,"EditarPosteo.html", {"formularioposteo":formularioposteo,"posteo":posteo,"imagen":mostrarImagen(request)})
        

#---------------- Eliminar posteo ----------------
@login_required
def eliminarPosteo(request):

    if request.method == 'POST':
        id = request.POST['id']
        posteo = get_object_or_404(Posteo, pk=id)
        if request.user.is_superuser or request.user == posteo.usuario_posteo:
            posteo.delete()
            return redirect('verposteo')
        else:   
            return render(request, 'VerPosteos.html',{"mensaje":"No estás autorizado para esta funciòn"})

    return redirect('verposteo')

#---------------- BUSCAR POSTEO ------------------------
@login_required
def buscar(request):
    buscar_por = request.GET.get("buscar_por")
    var1=request.GET ["titulo_posteo"]
    
    if buscar_por == "titulo_posteo":
        resultado = Posteo.objects.filter(titulo_posteo__icontains=var1)
    elif buscar_por == "subtitulo_posteo":
        resultado = Posteo.objects.filter(subtitulo_posteo__icontains=var1)
    elif buscar_por == "subtitulo2_posteo":
        resultado = Posteo.objects.filter(subtitulo2_posteo__icontains=var1)
    else:
        resultado = None
        return redirect("verposteo")
    return render(request,"ResultadoBusqueda.html", {"resultado":resultado,"imagen":mostrarImagen(request)})


#--------------------PAGINA POSTEO ------------------------------
@login_required
def paginaPosteo(request,id):

    paginaposteo = Posteo.objects.get(id=id)

    return render(request, "PaginaPosteo.html",{"imagen":mostrarImagen(request), "paginaposteo":paginaposteo})
 