from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

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
    usuario_posteo_forms=forms.CharField(widget=forms.TextInput(), required=True, max_length=100)
    titulo_posteo_forms = forms.CharField(max_length=25)
    contenido_posteo_forms = RichTextField()
    imagen_posteo_forms = forms.ImageField()
    fecha_posteo_imagen_forms = forms.DateField()
    class Meta:
        model = Posteo
        fields=["usuario_posteo_forms","titulo_posteo_forms","contenido_posteo_forms","imagen_posteo_forms","fecha_posteo_imagen_forms"]
        help_texts = {k:"" for k in fields} 