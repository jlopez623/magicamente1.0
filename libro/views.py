from pipes import Template
#from unicodedata import name
from unittest import loader
from django.shortcuts import render, redirect
from django.http import HttpResponse
import datetime
from django.template import Template, Context, loader
from .forms import UserForm, TaskForm, QuiensoyForm

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError

from .models import Task, Cuestionario, Quiensoy
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

            return render(request, 'sign.html', {
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



def portada0(request):
    
    anterior= '/dashboard/'
    siguiente = '/portada1/'
    context = {"anterior": anterior, "siguiente": siguiente}
    return render(request, '001-portada.html', context )

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
    anterior= '/portada1/'
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

#@login_required
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
    
    anterior= '/agua02/'
    siguiente = '/grafica1'
    
    if request.method == request.POST:
        data = request.POST
        print(data)
        context = {"anterior": anterior, "siguiente": siguiente, 'data':data}
    else:
        context = {"anterior": anterior, "siguiente": siguiente}        

    return render(request, '16-agua03.html', context)

@login_required
def tabla(request):
    anterior= '/agua03/'
    siguiente = '/grafica2'
    context = {"anterior": anterior, "siguiente": siguiente}

    return render(request, 'tabla.html', context)

@login_required
def fomr1(request):
    return render(request, 'form1.html')

@login_required
def grafica1(request):
    anterior= '/agua03/'
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
    form = QuiensoyForm(request.POST or None)
    
    
    data= request.POST
    anterior= '/actuar1/'
    siguiente = '/quiensoy2/'
    label=0
    
            

            
        
    context = {"anterior": anterior, "siguiente": siguiente, 'form':form, 'label':label,}
    
    return render(request, '20-quien-soy1.html',context)

@login_required
def quiensoy2(request):
    anterior= '/quiensoy1/'
    siguiente = '/aguaport/'
    context = {"anterior": anterior, "siguiente": siguiente}
    
    return render(request, '20-quien-soy2.html',context)

@login_required
def aguaport(request):
    anterior= '/quiensoy2/'
    siguiente = '/agua001/'
    context = {"anterior": anterior, "siguiente": siguiente}
    
    return render(request, '21-paraviviragua.html',context)

@login_required
def agua001(request):
    anterior= '/aguaport/'
    siguiente = '/agua002/'
    context = {"anterior": anterior, "siguiente": siguiente}
    
    return render(request, '22-paraviviragua2.html',context)
    
@login_required
def agua002(request):
    anterior= '/agua001/'
    siguiente = '/tierra001/'
    context = {"anterior": anterior, "siguiente": siguiente}
    
    return render(request, '23-paraviviragua3.html',context)

@login_required
def tierra001(request):
    anterior= '/agua002/'
    siguiente = '/tierra002/'
    context = {"anterior": anterior, "siguiente": siguiente}
    
    return render(request, '24-tierra.html',context)

@login_required
def tierra002(request):
    anterior= '/tierra001/'
    siguiente = '/tierra003/'
    context = {"anterior": anterior, "siguiente": siguiente}
    
    return render(request, '25-tierra002.html',context)

@login_required
def tierra003(request):
    anterior= '/tierra002/'
    siguiente = '/tierra004/'
    context = {"anterior": anterior, "siguiente": siguiente}
    
    return render(request, '26-tierra003.html',context)

@login_required
def tierra004(request):
    anterior= '/tierra003/'
    siguiente = '/tierra005/'
    context = {"anterior": anterior, "siguiente": siguiente}
    
    return render(request, '27-tierra004.html',context)
@login_required
def tierra005(request):
    anterior= '/tierra004/'
    siguiente = '/tierra006/'
    context = {"anterior": anterior, "siguiente": siguiente}
    
    return render(request, '28-tierra005.html',context)

@login_required
def tierra006(request):
    anterior= '/tierra005/'
    siguiente = '/tierra007/'
    context = {"anterior": anterior, "siguiente": siguiente}
    
    return render(request, '29-tierra006.html',context)

@login_required
def tierra007(request):
    anterior= '/tierra006/'
    siguiente = '/tierra008/'
    context = {"anterior": anterior, "siguiente": siguiente}
    
    return render(request, '30-tierra007.html',context)

@login_required
def tierra008(request):
    anterior= '/tierra007/'
    siguiente = '/tierra009/'
    context = {"anterior": anterior, "siguiente": siguiente}
    
    return render(request, '31-tierra008.html',context)

@login_required
def tierra009(request):
    anterior= '/tierra008/'
    siguiente = '/tierra010/'
    context = {"anterior": anterior, "siguiente": siguiente}
    
    return render(request, '32-tierra009.html',context)

@login_required
def tierra010(request):
    anterior= '/tierra009/'
    siguiente = '/tierra011/'
    context = {"anterior": anterior, "siguiente": siguiente}
    
    return render(request, '33-tierra010.html',context)

@login_required
def tierra011(request):
    anterior= '/tierra010/'
    siguiente = '/aire01/'
    context = {"anterior": anterior, "siguiente": siguiente}
    
    return render(request, '34-tierra011.html',context)

@login_required
def aire01(request):
    anterior= '/tierra011/'
    siguiente = '/aire02/'
    context = {"anterior": anterior, "siguiente": siguiente}
    
    return render(request, '35-aire01.html',context)

@login_required
def aire02(request):
    anterior= '/aire01/'
    siguiente = '/aire03/'
    context = {"anterior": anterior, "siguiente": siguiente}
    
    return render(request, '36-aire02.html',context)

@login_required
def aire03(request):
    anterior= '/aire02/'
    siguiente = '/aire04/'
    context = {"anterior": anterior, "siguiente": siguiente}
    
    return render(request, '37-aire03.html',context)

@login_required
def aire04(request):
    anterior= '/aire03/'
    siguiente = '/aire05/'
    context = {"anterior": anterior, "siguiente": siguiente}
    

    return render(request, '38-aire04.html', context)

@login_required
def aire05(request):
    anterior= '/aire03/'
    siguiente = '/aire06/'
    context = {"anterior": anterior, "siguiente": siguiente}
    

    return render(request, '39-aire05.html', context)

@login_required
def aire06(request):
    anterior= '/aire05/'
    siguiente = '/aire07/'
    context = {"anterior": anterior, "siguiente": siguiente}
    return render(request, '40-aire06.html', context)


@login_required
def aire07(request):
    anterior= '/aire06/'
    siguiente = '/aire08/'
    context = {"anterior": anterior, "siguiente": siguiente}
    return render(request, '41-aire07.html', context)

@login_required
def aire08(request):
    anterior= '/aire07/'
    siguiente = '/aire09/'
    context = {"anterior": anterior, "siguiente": siguiente}
    return render(request, '42-aire08.html', context)

@login_required
def aire09(request):
    anterior= '/aire08/'
    siguiente = '/aire10/'
    context = {"anterior": anterior, "siguiente": siguiente}
    return render(request, '43-aire09.html', context)


@login_required
def aire10(request):
    anterior= '/aire09/'
    siguiente = '/aire11/'
    context = {"anterior": anterior, "siguiente": siguiente}
    return render(request, '44-aire10.html', context)

@login_required
def aire11(request):
    anterior= '/aire10/'
    siguiente = '/aire12/'
    context = {"anterior": anterior, "siguiente": siguiente}
    return render(request, '45-aire11.html', context)

@login_required
def aire12(request):
    anterior= '/aire11/'
    siguiente = '/aire13/'
    context = {"anterior": anterior, "siguiente": siguiente}
    return render(request, '46-aire12.html', context)

@login_required
def aire13(request):
    anterior= '/aire12/'
    siguiente = '/aire14/'
    context = {"anterior": anterior, "siguiente": siguiente}
    return render(request, '47-aire13.html', context)

@login_required
def aire14(request):
    anterior= '/aire13/'
    siguiente = '/aire15/'
    context = {"anterior": anterior, "siguiente": siguiente}
    return render(request, '48-aire14.html', context)

@login_required
def aire15(request):
    anterior= '/aire14/'
    siguiente = '/fuego01/'
    context = {"anterior": anterior, "siguiente": siguiente}
    return render(request, '49-aire15.html', context)

@login_required
def fuego01(request):
    anterior= '/aire15/'
    siguiente = '/fuego02/'
    context = {"anterior": anterior, "siguiente": siguiente}
    return render(request, '50-fuego01.html', context)

@login_required
def fuego02(request):
    anterior= '/fuego01/'
    siguiente = '/fuego03/'
    context = {"anterior": anterior, "siguiente": siguiente}
    return render(request, '51-fuego02.html', context)

@login_required
def fuego03(request):
    anterior= '/fuego02/'
    siguiente = '/fuego04/'
    context = {"anterior": anterior, "siguiente": siguiente}
    return render(request, '52-fuego03.html', context)


@login_required
def fuego04(request):
    anterior= '/fuego03/'
    siguiente = '/fuego05/'
    context = {"anterior": anterior, "siguiente": siguiente}
    return render(request, '53-fuego04.html', context)

@login_required
def fuego05(request):
    anterior= '/fuego04/'
    siguiente = '/fuego06/'
    context = {"anterior": anterior, "siguiente": siguiente}
    return render(request, '54-fuego05.html', context)











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

@login_required
def tablaPrueba(request):
    cuestionario= Cuestionario.objects.all()
   
    print(cuestionario)
    """context= {'cuestionario':Cuestionario}"""
    return render (request, 'tabla.html', {"cuestionario":cuestionario})
