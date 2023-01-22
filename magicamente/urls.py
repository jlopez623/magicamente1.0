"""magicamente URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
#from django.contrib.auth.views import login, logout_then_login
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from libro.views import agradecimientos,  cargarHtml, magia2, parametros,  portada, shortcut, personaImportante, signout, signin, crearTask
from libro.views import prologo1, prologo2, introduccion, introduccion2, magia1, magia2, magia3, fomr1, magia4
from libro.views import agua01, agua02, agua03, usuario,  crearUsuario, home, signup, dashboard, task, taskDetail, complete, delete, completadas, grafica1, tabla, grafica2, actuar1, quiensoy1, quiensoy2, aguaport, agua001, agua002, tierra001, tierra002, tierra003, tierra004, tierra005, tierra006, tierra007, tierra008, tierra009, tierra010, tierra011, aire01, aire02, aire03, aire04, aire05, aire06, aire07, aire08, aire09, aire10, aire11, aire12, aire13, aire14, aire15, fuego01, fuego02, fuego03, fuego04, portada0, fuego05, tablaPrueba


urlpatterns = [

    path('accounts/', include('django.contrib.auth.urls')),
    path('creartarea/', crearTask, name='creartarea'),
    path('detalletarea/<int:task_id>/', taskDetail, name='taskdetail'),
    path('detalletarea/<int:task_id>/completed', complete, name='completada'),
    path('detalletarea/<int:task_id>/eliminar', delete, name='eliminar'),
    path('admin/', admin.site.urls),
    path('signup/', signup, name="signup"),
    path('logout/', signout, name='logout'),
    path('login/', signin, name='login'),
    path('', home, name='home'),
    path('task/', task , name="tareas"),
    path('completadas/', completadas , name="completadas"),
    path('home/', home),
    path('dashboard/', dashboard, name='dashboard'),
    path('portada1/', portada, name="portada"),
    path('portada0/', portada0, name="portada0"),
    path('parametros/', parametros),
    path('cargador/', cargarHtml),
    path('shortcut/', shortcut),
    path('agradecimientos/', agradecimientos, name='agradecimientos'),
    path('la-persona-importante/', personaImportante, name="yo"),
    path('prologo1/', prologo1, name='prologo1'),
    path('prologo2/', prologo2, name='prologo2'),
    path('intro1/', introduccion, name='intro1'),
    path('intro2/', introduccion2, name="intro2"),
    path('magia01/', magia1, name="magia01"),
    path('magia02/', magia2, name='magia03'),
    path('magia03/', magia3),
    path('magia04/', magia4),
    path('agua01/', agua01),
    path('agua02/', agua02),
    path('agua03/', agua03),
    path('registro/', crearUsuario, name='registro'),
    path('grafica1/', grafica1, name='grafica1'),
    path('tabla/', tabla, name='tabla'),
    path('grafica2/', grafica2, name='grafica2'),
    path('actuar1/', actuar1, name='actuar1'),
    path('quiensoy1/', quiensoy1, name='quiensoy1'),
    path('quiensoy2/', quiensoy2, name='quiensoy2'),
    path('aguaport/', aguaport, name='aguaport'),
    path('agua001/', agua001, name='agua001'),
    path('agua002/', agua002, name='agua002'),
    path('tierra001/', tierra001, name='tierra001'),
    path('tierra002/', tierra002, name='tierra002'),
    path('tierra003/', tierra003, name='tierra003'),
    path('tierra004/', tierra004, name='tierra004'),
    path('tierra005/', tierra005, name='tierra005'),
    path('tierra006/', tierra006, name='tierra006'),
    path('tierra007/', tierra007, name='tierra007'),
    path('tierra008/', tierra008, name='tierra008'),
    path('tierra009/', tierra009, name='tierra009'),
    path('tierra010/', tierra010, name='tierra010'),
    path('tierra011/', tierra011, name='tierra011'),
    path('aire01/', aire01, name='aire01'),
    path('aire02/', aire02, name='aire02'),
    path('aire03/', aire03, name='aire03'),
    path('aire04/', aire04, name='aire04'),
    path('aire05/', aire05, name='aire05'),
    path('aire06/', aire06, name='aire06'),
    path('aire07/', aire07, name='aire07'),
    path('aire08/', aire08, name='aire08'),
    path('aire09/', aire09, name='aire09'),
    path('aire10/', aire10, name='aire10'),
    path('aire11/', aire11, name='aire11'),
    path('aire12/', aire12, name='aire12'),
    path('aire13/', aire13, name='aire13'),
    path('aire14/', aire14, name='aire14'),
    path('aire15/', aire15, name='aire15'),
    path('fuego01/', fuego01, name='fuego01'),
    path('fuego02/', fuego02, name='fuego02'),
    path('fuego03/', fuego03, name='fuego03'),
    path('fuego04/', fuego04, name='fuego04'),
    path('fuego05/', fuego05, name='fuego05'),
    path('tabla/', tablaPrueba, name='tabla'),
    
    
    path('form1/', fomr1),
    path('form1/user/', usuario)



] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
