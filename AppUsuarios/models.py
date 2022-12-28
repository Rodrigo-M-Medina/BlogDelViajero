from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
# Create your models here.
class Posteo(models.Model):
    usuario_posteo = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo_posteo = models.CharField(max_length=25)
    contenido_posteo = RichTextField(blank=True,null=True)
    imagen_posteo = models.ImageField(upload_to='Imagen', null=True, blank=True)
    fecha_posteo_imagen = models.DateField(auto_now_add=True)    
