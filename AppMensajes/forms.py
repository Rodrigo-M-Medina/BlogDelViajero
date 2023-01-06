from django import forms
from .models import *


#--------------------- MENSAJERIA -----------------------


class MensajeForm(forms.ModelForm):#solo necesito traer por meta el model Chat y sus field 
    class Meta:
        model = Chat
        fields = ['entrada', 'mensaje']
