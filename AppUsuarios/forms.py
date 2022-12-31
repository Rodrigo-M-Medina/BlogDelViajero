from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
from ckeditor.widgets import CKEditorWidget


class FormUsuario(UserCreationForm):
    nombre = forms.CharField(max_length=50)
    email = forms.EmailField()
    password1 = forms.CharField(label="Ingrese Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repita Contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        help_texts = {k:"" for k in fields}


class FormEditarUsuario(UserCreationForm):
    nombre = forms.CharField(max_length=50)
    email = forms.EmailField(label="ingrese su email")
    password1 = forms.CharField(label="Ingrese Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repita Contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        help_texts = {k:"" for k in fields}

class PosteoForm(forms.Form):
    titulo_posteo = forms.CharField(label="Ingrese título")
    contenido_posteo = forms.CharField(widget=CKEditorWidget())
    imagen_post = forms.ImageField(label="Imagen")

    class Meta:
        model = Posteo
        fields = ["titulo_posteo", "contenido_posteo", "imagen_post"]

class ImagenPerfilForm(forms.Form):
    imagen=forms.ImageField(label="Imagen")