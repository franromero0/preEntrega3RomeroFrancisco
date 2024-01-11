from django.shortcuts import render
from burger.models import Pedido, Resena, Recomendacion, Hamburguesa, Bebida, Combo
from burger.forms import *
# Create your views here.

def inicio(request):
    
    return render(request, "burger/inicio.html")



# Vistas para ver los productos creados de la empresa

def ver_hamburguesas(request):
    return render(request, "burger/hamburguesas.html")


def ver_bebidas(request):
    return render(request, "burger/bebidas.html")

def ver_combos(request):
      return render(request, "burger/combos.html")



#Formularios para Create data

def pedidos(request ):
    
    if request.method == "POST":
        pedido = Pedido(nombre=request.POST["nombre"],
                              email=request.POST["email"],
                              direccion=request.POST["direccion"],
                              sucursal=request.POST["sucursal"],
                              bebida=request.POST["bebida"],
                              hamburguesa=request.POST["hamburguesa"],
                              cant_blends=request.POST["cant_blends"],
                              cant_hamburguesas=request.POST["cant_hamburguesas"],
                              metodo_pago=request.POST["metodo_pago"],
                              observacion=request.POST["observacion"])
        pedido.save()
        return render(request, "burger/pedido_realizado.html")
        
    else:
         return render(request, "burger/pedidos.html")
     
# Vista para que los clientes realicen una devolucion con respecto a la comida del momento --- Diferente a sugerencia    
def realizar_resena(request):
    if request.method == "POST":    
        formulario = ResenaFormulario(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            nueva_resena = Resena(nombre=info["nombre"],
                            email=info["email"],
                            resena=info["resena"])
            nueva_resena.save()
            resenas_totales = Resena.objects.all()
        
            return render(request, "burger/valoraciones.html", {"valoraciones":resenas_totales})
    else:
        formulario = ResenaFormulario()
        return render(request, "burger/realizar_reseña.html", {"mi_formu": formulario})
    
 # Ver las reseñas hechas por clientes

def valoraciones(request):
    resenas_totales = Resena.objects.all()
    
    return render(request, 'burger/valoraciones.html', {"valoraciones":resenas_totales})   


# Vista para que los clientes realicen sugerencias con respecto al servicio --- Diferente a reseña
def realizar_sugerencia(request):
    if request.method == "POST":    
        formulario = RecomendacionFormulario(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            nueva_sugerencia = Recomendacion(nombre=info["nombre"],
                                             email=info["email"],
                                             recomendacion=info["recomendacion"]
                                             )
            nueva_sugerencia.save()
            sugerencias_totales = Recomendacion.objects.all()
            return render(request, "burger/sugerencias.html", {"sugerencias":sugerencias_totales})
        
    else:
            formulario = RecomendacionFormulario()
            return render(request, "burger/realizar_sugerencia.html",{"mi_formu": formulario})
        

def sugerencias(request):
    sugerencias_totales = Recomendacion.objects.all()
    
    return render(request, 'burger/sugerencias.html', {"sugerencias":sugerencias_totales})   

 # Views para que los administradores o en este caso cualquier usuario agregue una hamburguesa y bebebida  
   
def agregar_burger(request):
    if request.method == "POST":
        formulario= HamburguesaFormulario(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data #Para tenerlos en clase dict
            nueva_burger = Hamburguesa(nombre=info["nombre"],
                                       descripcion=info["descripcion"],
                                       precio=info["precio"])
            nueva_burger.save()
            return render(request,"burger/inicio.html")
        
            
    else: 
        formulario = HamburguesaFormulario() #Si la persona no hizo click en boton enviar mostraremos un formulario vacio
    return render(request, "burger/agregar_burger.html", {"mi_formu":formulario})
        

def agregar_bebida(request):
    if request.method == "POST":
        formulario= BebidaFormulario(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data #Para tenerlos en clase dict
            nueva_burger = Bebida(nombre=info["nombre"],
                                       descripcion=info["descripcion"],
                                       precio=info["precio"])
            nueva_burger.save()
            return render(request,"burger/inicio.html")
        
            
    else: 
        formulario = BebidaFormulario() #Si la persona no hizo click en boton enviar mostraremos un formulario vacio
    return render(request, "burger/agregar_bebida.html", {"mi_formu":formulario})
        
# Views para buscar info de la DB  -- GET



def busqueda_burger_nombre(request):
    return render(request, "burger/busqueda_burger.html")

def resultado_busqueda_burger_nombre(request):
    if request.method=="GET":
        nombre_busqueda = request.GET["busqueda_hambur"]
        resultados_burger = Hamburguesa.objects.filter(nombre__icontains=nombre_busqueda)
    
        return render(request, "burger/busqueda_hamburguesa_resultado.html", {"burgers": resultados_burger})
    else:
        return render(request, "burger/busqueda_burger.html")
    
    
def busqueda_bebida_nombre(request):
    return render(request, "burger/busqueda_bebida.html")

def resultado_busqueda_bebida_nombre(request):
    if request.method=="GET":
        nombre_busqueda = request.GET["busqueda_bebida"]
        resultados_bebidas = Bebida.objects.filter(nombre__icontains=nombre_busqueda)

        return render(request, "burger/busqueda_bebida_resultado.html", {"bebidas": resultados_bebidas})
    else:
        return render(request, "burger/busqueda_bebida.html")



#Buscar sugerencias especificas en la DB por nombre o palabra clave


def busqueda_sugerencia(request):
    return render(request, "burger/busqueda_sugerencia.html")

def resultado_busqueda_sugerencia(request):
    if request.method=="GET":
        if request.GET["busqueda__nombre_sugerencia"]:
            nombre_busqueda = request.GET["busqueda__nombre_sugerencia"]
            resultados = Recomendacion.objects.filter(nombre__icontains=nombre_busqueda)
        
            return render(request, "burger/resultados_sugerencias.html", {"sugerencias": resultados})
        elif request.GET["busqueda__palabra_sugerencia"]:
            palabra_busqueda = request.GET["busqueda__palabra_sugerencia"]
            resultados = Recomendacion.objects.filter(recomendacion__icontains=palabra_busqueda)
    
            return render(request, "burger/resultados_sugerencias.html", {"sugerencias": resultados})
    else:
        return render(request, "burger/busqueda_sugerencia.html")

 


