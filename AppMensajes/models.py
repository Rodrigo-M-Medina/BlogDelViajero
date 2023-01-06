from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

# Create your models here.
#----------------- Modelo para Mensajes  ---------------
class Chat(models.Model):
    salida = models.ForeignKey(User, on_delete=models.CASCADE, related_name='salida') #related_name en teoria me deja darle un field
    entrada = models.ForeignKey(User, on_delete=models.CASCADE, related_name='entrada')
    mensaje = RichTextField(blank=True, null=True)
    tiempo = models.DateTimeField(auto_now_add=True)
    leido = models.BooleanField(default=False)