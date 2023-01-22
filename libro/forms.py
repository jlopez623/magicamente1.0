from socket import fromshare
from django import forms
from .models import Usuario, Task, Cuestionario, Quiensoy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm


class QuiensoyForm (forms.ModelForm):
    class Meta:
        model = Quiensoy
        fields = '__all__'

class CuestionarioForm (forms.ModelForm):
    class Meta:
        model = Cuestionario
        fields = '__all__'

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields= ['title', 'descripción', 'important']


class UserForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'


class RegistrarForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email','password1','password2', 'first_name', 'email']