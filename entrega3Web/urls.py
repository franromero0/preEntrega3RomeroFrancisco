"""
URL configuration for entrega3Web project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from burger.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    
    #URLs Burger Apps
    path("", inicio),
    
    #URLs para los formularios o para que el usuario ingrese info (POST)
    path('pedido/', pedidos, name="pedido"),
    path('reseña/', realizar_resena, name="resena"),
    path('sugerencia/', realizar_sugerencia, name="sugerencia"),
    
    #URLs para ver informacion reseñas/sugerencias
    path('valoraciones/', valoraciones, name='valoraciones'),
    path('recomendaciones/', sugerencias, name='recomendaciones'),
    
    
    
    #URLs para ver productos  
    path('bebidas', ver_bebidas, name="bebidas"),
    path('hamburguesas', ver_hamburguesas, name="hamburguesas" ),
    path('combos', ver_combos, name = "combos"),
    
    #URLs para agregar productos
     path('agregarBurger', agregar_burger, name="agregar hamburguesas" ),
     path('agregarBebida', agregar_bebida, name="agregar bebidas" ),
    
    #URLs para buscar productos
    path('buscarHamburguesa/', busqueda_burger_nombre, name="buscar_hamburguesas"),
    path('resultadosHamburguesa/', resultado_busqueda_burger_nombre),
    path('buscarBebida/', busqueda_bebida_nombre),
    path('resultadosBebida/', resultado_busqueda_bebida_nombre),
    path('buscarSugerencia/', busqueda_sugerencia),
    path('resultadosSugerencia/', resultado_busqueda_sugerencia),
    
]
