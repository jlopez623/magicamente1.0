from socket import fromshare
from django import forms
from .models import Usuario
from django.contrib.auth.forms import UserCreationForm

class UserForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'


class RegistrarForm(UserCreationForm):
    pass 