from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User




#------------ Modelo de Posteos ---------------


class Posteo(models.Model):
    usuario_posteo = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo_posteo = models.CharField(max_length=40)
    subtitulo_posteo = models.CharField(max_length=40,default='Provincia')
    subtitulo2_posteo = models.CharField(max_length=40,default='Pais')
    contenido_posteo = RichTextField(blank=True,null=True)
    imagen_post = models.ImageField(upload_to='posteos', blank=True)
    fecha_posteo_imagen = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.titulo_posteo   
 
#----------- Modelo para imagen de perfil
class ImagenPerfil(models.Model):
    imagen=models.ImageField(upload_to='Perfil')
    user=models.ForeignKey(User, on_delete=models.CASCADE)


#---------- Modelo para biografia ---------
class Biografia(models.Model):
    usuarioBio = models.ForeignKey(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=800)

    def __str__(self):
        return self.bio


 




 
