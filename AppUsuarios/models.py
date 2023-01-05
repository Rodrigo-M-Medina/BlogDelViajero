from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User


#----------------- Modelo para Mensajes  ---------------
class Chat(models.Model):
    salida = models.ForeignKey(User, on_delete=models.CASCADE, related_name='salida') #related_name en teoria me deja darle un field
    entrada = models.ForeignKey(User, on_delete=models.CASCADE, related_name='entrada')
    mensaje = RichTextField(blank=True, null=True)
    tiempo = models.DateField(blank=True, null=True)
    leido = models.BooleanField(default=False)

#------------ Modelo de Posteos ---------------


class Posteo(models.Model):
    usuario_posteo = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo_posteo = models.CharField(max_length=40)
    subtitulo_posteo = models.CharField(max_length=40,default='hola')
    contenido_posteo = RichTextField(blank=True,null=True)
    imagen_post = models.ImageField(upload_to='posteos')
    fecha_posteo_imagen = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.titulo_posteo   
 

class ImagenPerfil(models.Model):
    imagen=models.ImageField(upload_to='Perfil')
    user=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo_posteo
 




 
