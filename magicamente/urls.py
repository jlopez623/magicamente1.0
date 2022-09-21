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
from libro.views import agradecimientos,  cargarHtml, magia2, parametros,  portada, shortcut, personaImportante
from libro.views import prologo1, prologo2, introduccion, introduccion2, magia1, magia2, magia3, fomr1, usuario1, magia4
from libro.views import agua01, agua02, agua03, usuario, camera, crearUsuario, home




urlpatterns = [
    
    path('accounts/', include('django.contrib.auth.urls') ),
    
    path('admin/', admin.site.urls),

  
    path('/', home),
    path('portada1/', portada),
    path('parametros/', parametros),
    path('cargador/', cargarHtml),
    path('shortcut/', shortcut),
    path('agradecimientos/', agradecimientos),
    path('la-persona-importante/', personaImportante),
    path('prologo1/', prologo1),
    path('prologo2/', prologo2),
    path('intro1/', introduccion),
    path('intro2/', introduccion2),
    path('magia01/', magia1),
    path('magia02/', magia2),
    path('magia03/', magia3),
    path('magia04/', magia4),
    path('agua01/', agua01),
    path('agua02/', agua02),
    path('agua03/', agua03),
    path('users/', usuario),
    path('registro/', crearUsuario, name='registro' ),
    path('yo/', camera),

    path('form1/', fomr1),
    path('form1/user/', usuario)
  

    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
