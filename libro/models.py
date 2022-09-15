from multiprocessing.sharedctypes import Value
from django.db import models

# Create your models here.
class CodeBook(models.Model):
    code=models.CharField(max_length=10)
    def __str__(self):
        return self.code

class Usuario (models.Model):
    
    first_name =models.CharField(max_length=20)
    last_name =models.CharField(max_length=20)
    email =models.EmailField(max_length=50)
    
    
    def __str__(self):
        return self.first_name, self.email, self.last_name
        
    
    
    