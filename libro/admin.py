from django.contrib import admin

# Register your models here.
from libro.models import CodeBook, Usuario

admin.site.register(CodeBook)
admin.site.register(Usuario)

        