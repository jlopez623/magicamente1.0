from pipes import Template
#from unicodedata import name
from unittest import loader



from django.shortcuts import render, redirect
from django.http import HttpResponse
import datetime
from django.template import Template, Context, loader
from .forms import UserForm, TaskForm

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from .forms import TaskForm
from .models import Task
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.contrib.auth.decorators import login_required

# request realizar peticion
# httpResponse enviar respuesta protocolo http

# Create your views here.


def signup(request):

    if request.method == 'GET':
        print('enviando formulario')
    else:
        if request.POST['password1'] == request.POST['password2']:
            # reg user
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'], first_name = request.POST['first_name'], last_name = request.POST['last'], email=request.POST['email'])
                user.save()
                login(request, user)
                return redirect('dashboard')

            except IntegrityError:
                return render(request, 'registration/signup.html', {
                    'form': UserCreationForm,
                    "error": 'usuario ya existe'
                })

        return render(request, 'registration/signup.html', {
            'form': UserCreationForm,
            "error": 'Las contraseñas no coinciden'
        })
    return render(request, 'registration/signup.html', {
        'form': UserCreationForm,
    })


@login_required
def dashboard(request):
    return render(request, 'userdashboard.html')


@login_required
def signout(request):
    logout(request)
    return redirect('home')


def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {'formlogin': AuthenticationForm})

    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        print(request.POST)

        if user is None:

            return render(request, 'signn.html', {
                'formlogin': AuthenticationForm,
                'error': 'Usuario o contraseña incorrectos'
            })
        else:
            login(request, user)
            return redirect('dashboard')


@login_required
def crearTask(request):

    if request.method == 'GET':
        return render(request, 'createTask.html', {
            'form': TaskForm
        })
    else:
        try:
            form = TaskForm(request.POST)  # toma los datos ingresados +/-
            newTask = form.save(commit=False)
            newTask.user = request.user
            newTask.save()
            return redirect('dashboard')
        except ValueError:
            return render(request, 'createTask.html', {
                'form': TaskForm,
                'error': 'Ingresa datos validos'
            })


@login_required
def task(request):
    tasks = Task.objects.filter(user=request.user,  datecompleted__isnull=True)
    return render(request, 'task.html', {'tasks': tasks})


@login_required
def completadas(request):
    tasks = Task.objects.filter(
        user=request.user, datecompleted__isnull=False).order_by('-datecompleted')
    return render(request, 'task.html', {'tasks': tasks})


@login_required
def taskDetail(request, task_id):
    if request.method == 'GET':
        print(task_id)
        task = get_object_or_404(Task, pk=task_id, user=request.user)
        form = TaskForm(instance=task)
        return render(request, 'taskdetail.html', {'task': task, 'form': form})
    else:
        try:
            print(request.POST)
            task = get_object_or_404(Task, pk=task_id, user=request.user)
            form = TaskForm(request.POST, instance=task)
            form.save()
            print('lelgo')
            return redirect('task.html')
        except ValueError:
            error = 'revisa los valores ingresados'
            return render(request, 'taskdetail.html', {'task': task, 'form': form, 'error': error})


@login_required
def complete(request, task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    if request.method == 'POST':
        task.datecompleted = timezone.now()
        task.save()
        return redirect('tareas')  # nombre de vista 'tareas=task.khtml'


@login_required
def delete(request, task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('tareas')

def portada(request):

    anterior= '/dashboard/'
    siguiente = '/agradecimientos/'
    context = {"anterior": anterior, "siguiente": siguiente}
    return render(request, '01portada.html', context )

def parametros(request):


    menulibro = {"esto es pg": "1"}
    nombre_usuario = "usuario"
    date = datetime.datetime.now()
    plantilla = open(
        "D:/jlopezwebs/Gonzalo/magicamente/libro/templates/plantilla parametros.html")
    # load template
    template = Template(plantilla.read())
    plantilla.close()
    context = Context({"user": nombre_usuario, "fecha": date, "menu": menulibro})
    documento = template.render(context)
    return HttpResponse(documento)


def cargarHtml(request):
    menulibro = ["item1", "item2", "item3"]
    nombre_usuario = "usuario"
    date = datetime.datetime.now()

    plantilla = loader.get_template('plantilla parametros.html')
    document = plantilla.render(
        {"user": nombre_usuario, "fecha": date, "menu": menulibro})
    return HttpResponse(document)


def shortcut(request):
    menulibro = ["item1", "item2", "item3"]
    nombre_usuario = "usuario"
    date = datetime.datetime.now()

    return render(request, 'plantilla parametros.html', {"user": nombre_usuario, "fecha": date, "menu": menulibro})

@login_required
def agradecimientos(request):
    image = '{% static "img/p3/hoja3.pNG" %}'
    anterior= '/agradecimientos/'
    siguiente = '/la-persona-importante/'
    context = {"anterior": anterior, "siguiente": siguiente}
    return render(request, '04-agradecimientos-indice.html', context)

@login_required
def personaImportante(request):
    anterior= '/agradecimientos/'
    siguiente = '/prologo1/'
    context = {"anterior": anterior, "siguiente": siguiente}
    return render(request, '05-personaportada.html', context)

@login_required
def prologo1(request):

    anterior= '/la-persona-importante/'
    siguiente = '/prologo2/'
    context = {"anterior": anterior, "siguiente": siguiente}

    return render(request, '06-prologo1.html', context)


def home(request):
    return render(request, 'home.html')

@login_required
def prologo2(request):
    anterior= '/prologo1/'
    siguiente = '/intro1/'
    context = {"anterior": anterior, "siguiente": siguiente}
    return render(request, '07-prologo2.html',context)

@login_required
def introduccion(request):
    anterior= '/prologo2/'
    siguiente = '/intro2/'
    context = {"anterior": anterior, "siguiente": siguiente}  
    return render(request, '08-introduccion1.html',context)

@login_required
def introduccion2(request):
    anterior= '/intro1/'
    siguiente = '/magia01/'
    context = {"anterior": anterior, "siguiente": siguiente}  
    return render(request, '09-introduccion2.html', context)

@login_required
def magia1(request):
    anterior= '/intro2/'
    siguiente = '/magia02/'
    context = {"anterior": anterior, "siguiente": siguiente}
    return render(request, '10-la-magia1.html', context)

@login_required
def magia2(request):
    anterior= '/magia01/'
    siguiente = '/magia03/'
    context = {"anterior": anterior, "siguiente": siguiente}
    return render(request, '10-la-magia2.html', context)

@login_required
def magia3(request):
    anterior= '/magia02/'
    siguiente = '/magia04/'
    context = {"anterior": anterior, "siguiente": siguiente}
    return render(request, '10-magia03.html',context)

@login_required
def magia4(request):
    anterior= '/magia03/'
    siguiente = '/agua01/'
    context = {"anterior": anterior, "siguiente": siguiente}
    return render(request, '10-magia04.html', context)

@login_required
def agua01(request):
    anterior= '/magia04/'
    siguiente = '/agua02/'
    context = {"anterior": anterior, "siguiente": siguiente}
    return render(request, '14-agua01.html', context)

@login_required
def agua02(request):
    anterior= '/agua01/'
    siguiente = '/agua03/'
    context = {"anterior": anterior, "siguiente": siguiente}
    return render(request, "15-agua-02.html", context)

@login_required
def agua03(request):
    anterior= '/magia02/'
    siguiente = '/grafica1'
    context = {"anterior": anterior, "siguiente": siguiente}

    return render(request, '16-agua03.html', context)

@login_required
def fomr1(request):
    return render(request, 'form1.html')

@login_required
def grafica1(request):
    anterior= '/magia03/'
    siguiente = '/grafica2/'
    context = {"anterior": anterior, "siguiente": siguiente}
    
    return render(request, '17-grafica.html',context)

@login_required
def grafica2(request):
    anterior= '/grafica1/'
    siguiente = '/actuar1/'
    context = {"anterior": anterior, "siguiente": siguiente}
    
    return render(request, '18-grafica.html',context)

@login_required
def actuar1(request):
    anterior= '/grafica2/'
    siguiente = '/quiensoy1/'
    context = {"anterior": anterior, "siguiente": siguiente}
    
    return render(request, '19-actuar1.html',context)

@login_required
def quiensoy1(request):
    anterior= '/actuar1/'
    siguiente = '/quiensoy2/'
    context = {"anterior": anterior, "siguiente": siguiente}
    
    return render(request, '20-quien-soy1.html',context)

@login_required
def quiensoy2(request):
    anterior= '/quiensoy1/'
    siguiente = '/aguaport/'
    context = {"anterior": anterior, "siguiente": siguiente}
    
    return render(request, '20-quien-soy2.html',context)

@login_required
def aguaport(request):
    anterior= '/quiensoy1/'
    siguiente = '/aguaport/'
    context = {"anterior": anterior, "siguiente": siguiente}
    
    return render(request, '21-paraviviragua.html',context)

def usuario1(request):
    print("hola")
    mensaje = "hola %r" % request.GET["nombre"]
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
