from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
# Create your models here.
class Posteo(models.Model):
    usuario_posteo = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo_posteo = models.CharField(max_length=25)
    contenido_posteo = RichTextField(blank=True,null=True)
    imagen_post = models.ImageField(upload_to='posteos')
    fecha_posteo_imagen = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.titulo_posteo
 
