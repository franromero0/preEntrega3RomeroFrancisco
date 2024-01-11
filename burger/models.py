from django.db import models

# Create your models here.

class Pedido(models.Model):
    nombre = models.CharField(max_length=40)
    email = models.EmailField()
    direccion = models.CharField(max_length=40)
    sucursal = models.CharField(max_length=40)
    bebida =  models.CharField(max_length=40)
    hamburguesa = models.CharField(max_length=40)
    cant_blends = models.CharField(max_length=40)
    cant_hamburguesas = models.IntegerField()
    metodo_pago = models.CharField(max_length=40)
    observacion = models.TextField()
    
class Resena(models.Model):
    def __str__(self):
        return f"ID: {self.id}|  {self.resena}"
    nombre = models.CharField(max_length=40)
    email = models.EmailField()
    resena = models.CharField(max_length=500)
    

class Hamburguesa(models.Model):
    def __str__(self):
        return f"ID: {self.id}|  {self.nombre}"
    nombre = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=1000)
    precio = models.IntegerField()


class Bebida(models.Model):
    def __str__(self):
        return f"ID: {self.id}|  {self.nombre}"
    nombre = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=1000)
    precio = models.IntegerField()


class Combo(models.Model):
    def __str__(self):
        return f"ID: {self.id} | Disfruta {self.cantidad_burger} hamburguesas {self.nombre_burger} junto con {self.cantidad_bebida} {self.nombre_bebida}"
    cantidad_burger = models.IntegerField()
    cantidad_bebida = models.IntegerField()
    nombre_burger = models.CharField(max_length=40)
    nombre_bebida = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=1000)
    precio_combo = models.IntegerField()


class Recomendacion(models.Model):
    def __str__(self):
        return f"ID: {self.id}|  {self.recomendacion}"
    nombre = models.CharField(max_length=40)
    email = models.EmailField()
    recomendacion = models.CharField(max_length=1000)
    

    

    
    
    
