from multiprocessing.sharedctypes import Value
from django.db import models

# Create your models here.
class CodeBook(models.Model):
    code=models.CharField(max_length=10)
    def __str__(self):
        return self.code

class Usuario (models.Model):
    
    first_name =models.CharField(max_length=20, verbose_name='Nombre')
    last_name =models.CharField(max_length=20, verbose_name='Apellido')
    email =models.EmailField(max_length=50, verbose_name='Email')
    movil = models.CharField(max_length=10, verbose_name='Teléfono')
    birth = models.DateField(verbose_name="fecha de nacimiento",)
    password = models.CharField(max_length=50, verbose_name='contraseña')
     
    
    def __str__(self):
        return self.first_name
        
    
    
    