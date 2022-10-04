from socket import fromshare
from django import forms
from .models import Usuario, Task
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields= ['title', 'descripción', 'important']


class UserForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'


class RegistrarForm(UserCreationForm):
    pass