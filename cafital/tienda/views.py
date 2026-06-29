from django.shortcuts import render
from .models import Producto

def index(request):
    return render(request, 'tienda/index.html')

def productos(request):
    productos = Producto.objects.all()
    return render(request, 'tienda/productos.html', {'productos': productos})

def sobre_nosotros(request):
    return render(request, 'tienda/sobre_nosotros.html')

def contacto(request):
    return render(request, 'tienda/contacto.html')