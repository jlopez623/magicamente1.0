
from django.db import models
from django.contrib.auth.models import User
from .choices import sexo
from django.core.exceptions import ValidationError
#from .choices import codigo_libro

# Create your models here.


class CodeBook(models.Model):
    code = models.CharField(max_length=10,  # choices=codigo_libro
                            )
    disponible = models.BooleanField(default=True, verbose_name='disponible')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.code
# tablas para cuestionario:


class Cuestionario (models.Model):
    espiritual = models.CharField(verbose_name='Espiritual', default='0', max_length=3)
    fisica = models.CharField(verbose_name='Física' , default='0', max_length=3 )
    mental = models.CharField(verbose_name='Mental', default='0', max_length=3)
    emocional = models.CharField(verbose_name='Emocional', default='0', max_length=3)
    ludica = models.CharField(verbose_name='Lúdica', default='0', max_length=3)
    familiar = models.CharField(verbose_name='Familiar', default='0', max_length=3)
    social = models.CharField(verbose_name='Social', default='0', max_length=3)
    economica = models.CharField(verbose_name='Económica', default='0', max_length=3)
    ecologica = models.CharField(verbose_name='Ecológica', default='0', max_length=3)
    laboral = models.CharField(verbose_name='Laboral', default='0', max_length=3)
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return  self.user.email
    
class Quiensoy(models.Model):
    Quiensoy_id = models.IntegerField(primary_key=True)
    respuesta = models.CharField(max_length=300,null=True)
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
     
        
    
    
    def __str__(self):
        return self.respuesta
    
    


class Usuario (models.Model):

    first_name = models.CharField(max_length=20, verbose_name='Nombre')
    last_name = models.CharField(max_length=20, verbose_name='Apellido')
    email = models.EmailField(max_length=50, verbose_name='Email')
    movil = models.CharField(max_length=10, verbose_name='Teléfono', null=True)
    birth = models.DateField(verbose_name="fecha de nacimiento", null=True)
    password = models.CharField(max_length=50, verbose_name='contraseña')

    def __str__(self):
        return self.first_name


"""class Profiles_photo(models.Model):
    Photo = models.ImageField(verbose_name='photo', null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.user"""


class Task(models.Model):
    title = models.CharField(max_length=100)
    descripción = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    datecompleted = models.DateField(null=True)
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title + ' by ' + self.user.username


class Docente(models.Model):
    apellido_paterno = models.CharField(
        max_length=20, verbose_name='Apellido paterno')
    apellido_materno = models.CharField(
        max_length=20, verbose_name='Apellido Materno')
    nombres = models.CharField(max_length=20, verbose_name='Nombres')
    fecha_nacimiento = models.DateField(verbose_name='Fecha de nacimiento')
    sexo = models.CharField(max_length=1, choices=sexo, default='F')

    def nombre_completo(self):
        return "{} {}, {}".format(self.apellido_paterno, self.apellido_materno, self.nombres)

    def __str__(self):
        return self.nombre_completo()

    class Meta:
        verbose_name = 'Docente'
        verbose_name_plural = 'Docentes'
        db_table = 'docente'
        ordering = ['apellido_paterno', '-apellido_materno']
