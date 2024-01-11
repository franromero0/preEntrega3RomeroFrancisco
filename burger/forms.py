from django import forms


class PedidoFormulario(forms.Form):          #No se utilizó. Finalmente fue creado en html con el fin de maneter la estetica de la web.
    nombre = forms.CharField(max_length=40)
    email = forms.EmailField()
    direccion = forms.CharField(max_length=40)
    sucursal = forms.CharField(max_length=40)
    bebida =  forms.CharField(max_length=40)
    hamburguesa = forms.CharField(max_length=40)
    cant_blends = forms.CharField(max_length=40)
    cant_hamburguesas = forms.IntegerField()
    metodo_pago = forms.CharField(max_length=40)
    observacion = forms.CharField(max_length=150)
    
    
class ResenaFormulario(forms.Form):
    nombre = forms.CharField(max_length=40)
    email = forms.EmailField()
    resena = forms.CharField(max_length=170)
    
    
class RecomendacionFormulario(forms.Form):
    nombre = forms.CharField(max_length=150)
    email = forms.EmailField()
    recomendacion = forms.CharField(max_length=1000)
    

class HamburguesaFormulario(forms.Form):

    nombre = forms.CharField(max_length=40)
    descripcion = forms.CharField(max_length=1000)
    precio = forms.IntegerField()


class BebidaFormulario(forms.Form):

    nombre = forms.CharField(max_length=40)
    descripcion = forms.CharField(max_length=1000)
    precio = forms.IntegerField()


class ComboFormulario(forms.Form):

    cantidad_burger = forms.IntegerField()
    cantidad_bebida = forms.IntegerField()
    nombre_burger = forms.CharField(max_length=40)
    nombre_bebida = forms.CharField(max_length=40)
    descripcion = forms.CharField(max_length=1000)
    precio_combo = forms.IntegerField()