from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
from ckeditor.widgets import CKEditorWidget


#------------------------------------------ USUARIOS ------------------------------------------------

#------------- Formulario de registro usuario --------------
class FormUsuario(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Ingrese Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repita Contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        help_texts = {k:"" for k in fields}

#---------------------- Formulario Editar usuario -------------------
class FormEditarUsuario(UserCreationForm):
    nombre = forms.CharField(max_length=50)
    email = forms.EmailField(label="ingrese su email")
    password1 = forms.CharField(label="Ingrese Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repita Contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        help_texts = {k:"" for k in fields}

#--------------- Subir avatar ----------------
class ImagenPerfilForm(forms.Form):
    imagen=forms.ImageField(label="Imagen")



#-------------------------------------------- POSTEOS ---------------------------------------------------------

#----------------- Formulario para postear --------------------
class PosteoForm(forms.Form):
    titulo_posteo = forms.CharField(label="Ingrese destino")
    subtitulo_posteo = forms.CharField(label="Ingrese provincia de destino")
    subtitulo2_posteo =  forms.CharField(label="Ingrese pais de destino")
    contenido_posteo = forms.CharField(widget=CKEditorWidget())
    imagen_post = forms.ImageField(label="Imagen")

    class Meta:
        model = Posteo
        fields = ["titulo_posteo", "subtitulo_posteo","subtitulo2_posteo","contenido_posteo", "imagen_post"]


class BiografiaForm(forms.Form):
   bio = forms.CharField(widget=forms.Textarea(attrs={'id': 'bio-id'}))#por lo que me dice google con esto le puedo dar un id al form y editarlo en css