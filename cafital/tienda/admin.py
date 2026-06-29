from django.contrib import admin
from .models import Producto, CarritoItem, Pedido, DetallePedido, Contacto

admin.site.register(Producto)
admin.site.register(CarritoItem)
admin.site.register(Pedido)
admin.site.register(DetallePedido)
admin.site.register(Contacto)