from pipes import Template
from unittest import loader


from xml.dom.minidom import Document
from django.shortcuts import render
from django.http import HttpResponse
import datetime
from django.template import Template, Context, loader
from .forms import UserForm

from .models import Usuario

#request realizar peticion
#httpResponse enviar respuesta protocolo http

# Create your views here.

def portada(request):
    #open doc
    plantilla = open('D:/jlopezwebs/Gonzalo/magicamente/libro/templates/content.html')
    #load template
    template= Template(plantilla.read())
    plantilla.close()
    context = Context()
    documento = template.render(context)
    return HttpResponse(documento)

def parametros(request):
    menulibro = {"esto es pg":"1"}
    nombre_usuario = "usuario"
    date = datetime.datetime.now()
    plantilla = open("D:/jlopezwebs/Gonzalo/magicamente/libro/templates/plantilla parametros.html")
    #load template
    template= Template(plantilla.read())
    plantilla.close()
    context = Context({"user": nombre_usuario,"fecha": date, "menu":menulibro})
    documento = template.render(context)
    return HttpResponse(documento)

def cargarHtml(request):
    menulibro = ["item1","item2","item3"]
    nombre_usuario = "usuario"
    date = datetime.datetime.now()
    
    plantilla= loader.get_template('plantilla parametros.html')
    document = plantilla.render({"user": nombre_usuario,"fecha": date, "menu":menulibro})
    return HttpResponse(document)

def shortcut(request):
    menulibro = ["item1","item2","item3"]
    nombre_usuario = "usuario"
    date = datetime.datetime.now()

    return render(request, 'plantilla parametros.html',{"user": nombre_usuario,"fecha": date, "menu":menulibro})

def agradecimientos(request):
    image = '{% static "img/p3/hoja3.pNG" %}'
    context = Context({"imagenCentral":image})
    return render(request, '04-agradecimientos-indice.html')

def personaImportante(request):
    
    return render(request, '05-personaportada.html')

def prologo1(request):
    data={
        "titulo": 'hola',
        "siguiente": '07-prologo2.html/',
        "anterior": '05-personaportada.html'
    }
    
    return render(request,'06-prologo1.html',data)
def home(request):
    return render(request, 'home.html')
    
def prologo2(request):
    return render(request,'07-prologo2.html')
def introduccion(request):
    return render(request,'08-introduccion1.html')
def introduccion2(request):
    return render(request,'09-introduccion2.html')
def magia1(request):
    return render(request,'10-la-magia1.html')
def magia2(request):
    return render(request,'10-la-magia2.html')
def magia3(request):
    return render(request, '10-magia03.html')
def magia4(request):
    return render(request, '10-magia04.html')

def agua01(request):
    return render(request, '14-agua01.html')

def agua02(request):
    return render(request,"15-agua-02.html")

def agua03(request):

    return render(request,'16-agua03.html')


def fomr1 (request):
    return render(request,'form1.html')

def usuario1(request):
    print("hola")
    mensaje="hola %r" %request.GET ["nombre"]
    return HttpResponse(mensaje)
def usuario(request):
    return render(request, 'usuario.html')
    

def camera(request):
    return render(request, 'camera.html')


def crearUsuario(request):
    #data = {'form': RegistrarForm()}
    # data = UserForm.objects.all()
    formulario = UserForm(request.POST or None)
    return render(request, 'forms/registro.html', {'formulario': formulario})

