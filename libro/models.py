
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class CodeBook(models.Model):
    code=models.CharField(max_length=10)
    def __str__(self):
        return self.code

class Usuario (models.Model):
    
    first_name =models.CharField(max_length=20, verbose_name='Nombre')
    last_name =models.CharField(max_length=20, verbose_name='Apellido')
    email =models.EmailField(max_length=50, verbose_name='Email')
    movil = models.CharField(max_length=10, verbose_name='Teléfono',null=True)
    birth = models.DateField(verbose_name="fecha de nacimiento",null=True)
    password = models.CharField(max_length=50, verbose_name='contraseña')
     
    
    def __str__(self):
        return self.first_name
        
    
class Task(models.Model):
    title =  models.CharField(max_length=100)
    descripción = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    datecompleted = models.DateField(null=True)
    important = models.BooleanField(default=False) 
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title + ' by ' + self.user.username