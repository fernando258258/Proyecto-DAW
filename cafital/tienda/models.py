from django.db import models
from django.contrib.auth.models import User

class Producto(models.Model):
    FORMATOS = [
        ('capsulas', 'Cápsulas'),
        ('bolsitas', 'Bolsitas'),
        ('tarros', 'Tarros'),
    ]
    nombre = models.CharField(max_length=100)
    formato = models.CharField(max_length=20, choices=FORMATOS)
    descripcion = models.CharField(max_length=200)
    precio = models.IntegerField()
    stock = models.IntegerField(default=0)
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)

    def __str__(self):
        return self.nombre

class CarritoItem(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.cantidad} x {self.producto.nombre}"

class Pedido(models.Model):
    ESTADOS = [
        ('pendiente', 'Pendiente'),
        ('completado', 'Completado'),
        ('cancelado', 'Cancelado'),
    ]
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.IntegerField(default=0)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='pendiente')

    def __str__(self):
        return f"Pedido #{self.id} - {self.usuario.username}"

class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio_unitario = models.IntegerField()

    def __str__(self):
        return f"{self.cantidad} x {self.producto.nombre}"

class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    mensaje = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    leido = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.nombre} - {self.email}"