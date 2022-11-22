from email.policy import default
from wsgiref.validate import validator
from django.db import models
from django.conf import settings
from .validators import validar_nombre_categoria, validate_email


# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True, validators=[validar_nombre_categoria])

    def __str__(self):
        return self.nombre


class ProductUnits(models.TextChoices):
    UNITS = 'u', 'Unidades',
    DOCENS = 'd', 'Docenas'


class Producto(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    categoria = models.ForeignKey(Categoria, on_delete = models.CASCADE)
    descripcion = models.TextField()
    precio = models.DecimalField(decimal_places=2 , max_digits=6)
    unidades = models.CharField(max_length = 2, choices=ProductUnits.choices, default =ProductUnits.UNITS )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre


class Restaurante(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField()
    ubicacion = models.TextField(max_length=100)

    def __str__(self):
        return self.nombre


class EstadoPedido(models.TextChoices):
    RECIBIDO = 'r', 'Recibido',
    PREPARACION = 'p', 'Preparacion',
    CAMINO = 'c', 'Camino',
    ENTREGADO = 'e', 'Entregado',


class Pedido(models.Model):
    restaurante = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE,related_name="inventario_orden_restaurante")
    total = models.DecimalField(decimal_places=2 , max_digits=6)
    ubicacion = models.CharField(max_length=100)
    fecha = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length = 2, choices=EstadoPedido.choices, default =EstadoPedido.RECIBIDO )

class PedidoProducto(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete = models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete = models.CASCADE)
    cantidad = models.IntegerField(default=0)
    precio = models.CharField(max_length = 2, choices=ProductUnits.choices, default =ProductUnits.UNITS )


class Usuario(models.Model):
    user = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    email =  models.EmailField(max_length = 254, validators=[validate_email])
    ubicacion = models.TextField(max_length=100)
    tarjeta = models.IntegerField()
