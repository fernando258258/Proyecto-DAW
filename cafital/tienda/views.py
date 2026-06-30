from django.shortcuts import render
from .models import Producto
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import redirect
from .models import CarritoItem, Pedido, DetallePedido, Contacto
from django.contrib.auth.decorators import user_passes_test


def index(request):
    return render(request, 'tienda/index.html')

def productos(request):
    productos = Producto.objects.all()
    return render(request, 'tienda/productos.html', {'productos': productos})

def sobre_nosotros(request):
    return render(request, 'tienda/sobre_nosotros.html')

def contacto(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        email = request.POST['email']
        mensaje = request.POST['mensaje']
        Contacto.objects.create(nombre=nombre, email=email, mensaje=mensaje)
        return render(request, 'tienda/contacto.html', {'enviado': True})
    return render(request, 'tienda/contacto.html')

def registro(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Ese usuario ya existe.')
            return redirect('registro')

        user = User.objects.create_user(username=username, email=email, password=password)
        login(request, user)
        return redirect('index')

    return render(request, 'tienda/registro.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')
            return redirect('login')

    return render(request, 'tienda/login.html')

def logout_view(request):
    logout(request)
    return redirect('index')

@login_required
def agregar_carrito(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    item, created = CarritoItem.objects.get_or_create(
        usuario=request.user,
        producto=producto
    )
    if not created:
        item.cantidad += 1
        item.save()
    return redirect('carrito')

@login_required
def carrito(request):
    items = CarritoItem.objects.filter(usuario=request.user)
    total = sum(item.producto.precio * item.cantidad for item in items)
    return render(request, 'tienda/carrito.html', {'items': items, 'total': total})

@login_required
def eliminar_carrito(request, item_id):
    item = CarritoItem.objects.get(id=item_id, usuario=request.user)
    item.delete()
    return redirect('carrito')

@login_required
def confirmar_pedido(request):
    items = CarritoItem.objects.filter(usuario=request.user)

    if not items:
        return redirect('carrito')

    total = sum(item.producto.precio * item.cantidad for item in items)
    pedido = Pedido.objects.create(usuario=request.user, total=total)

    for item in items:
        DetallePedido.objects.create(
            pedido=pedido,
            producto=item.producto,
            cantidad=item.cantidad,
            precio_unitario=item.producto.precio
        )
        item.producto.stock -= item.cantidad
        item.producto.save()
        item.delete()

    return render(request, 'tienda/pedido_confirmado.html', {'pedido': pedido})

def es_admin(user):
    return user.is_superuser

@login_required
@user_passes_test(es_admin)
def admin_productos(request):
    productos = Producto.objects.all()
    pedidos_mes = Pedido.objects.count()
    mensajes_sin_leer = Contacto.objects.filter(leido=False).count()
    return render(request, 'tienda/admin_productos.html', {
        'productos': productos,
        'productos_count': productos.count(),
        'pedidos_mes': pedidos_mes,
        'mensajes_sin_leer': mensajes_sin_leer,
    })

@login_required
@user_passes_test(es_admin)
def admin_pedidos(request):
    pedidos = Pedido.objects.all().order_by('-fecha')
    pendientes = pedidos.filter(estado='pendiente').count()
    completados = pedidos.filter(estado='completado').count()
    total_ingresos = sum(p.total for p in pedidos)
    return render(request, 'tienda/admin_pedidos.html', {
        'pedidos': pedidos,
        'pendientes': pendientes,
        'completados': completados,
        'total_ingresos': total_ingresos,
    })

@login_required
@user_passes_test(es_admin)
def admin_mensajes(request):
    mensajes = Contacto.objects.all().order_by('-fecha')
    sin_leer = mensajes.filter(leido=False).count()
    return render(request, 'tienda/admin_mensajes.html', {
        'mensajes': mensajes,
        'total': mensajes.count(),
        'sin_leer': sin_leer,
    })

@login_required
@user_passes_test(es_admin)
def marcar_leido(request, mensaje_id):
    mensaje = Contacto.objects.get(id=mensaje_id)
    mensaje.leido = True
    mensaje.save()
    return redirect('admin_mensajes')

@login_required
@user_passes_test(es_admin)
def admin_producto_agregar(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        formato = request.POST['formato']
        descripcion = request.POST['descripcion']
        precio = request.POST['precio']
        stock = request.POST['stock']
        imagen = request.FILES.get('imagen')

        Producto.objects.create(
            nombre=nombre,
            formato=formato,
            descripcion=descripcion,
            precio=precio,
            stock=stock,
            imagen=imagen
        )
        return redirect('admin_productos')

    return render(request, 'tienda/admin_producto_form.html', {'accion': 'Agregar'})

@login_required
@user_passes_test(es_admin)
def admin_producto_editar(request, producto_id):
    producto = Producto.objects.get(id=producto_id)

    if request.method == 'POST':
        producto.nombre = request.POST['nombre']
        producto.formato = request.POST['formato']
        producto.descripcion = request.POST['descripcion']
        producto.precio = request.POST['precio']
        producto.stock = request.POST['stock']
        if request.FILES.get('imagen'):
            producto.imagen = request.FILES['imagen']
        producto.save()
        return redirect('admin_productos')

    return render(request, 'tienda/admin_producto_form.html', {'producto': producto, 'accion': 'Editar'})

@login_required
@user_passes_test(es_admin)
def admin_producto_eliminar(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    producto.delete()
    return redirect('admin_productos')

@login_required
@user_passes_test(es_admin)
def admin_pedido_editar(request, pedido_id):
    pedido = Pedido.objects.get(id=pedido_id)

    if request.method == 'POST':
        pedido.estado = request.POST['estado']
        pedido.save()
        return redirect('admin_pedidos')

    return render(request, 'tienda/admin_pedido_form.html', {'pedido': pedido})

@login_required
@user_passes_test(es_admin)
def admin_mensaje_eliminar(request, mensaje_id):
    mensaje = Contacto.objects.get(id=mensaje_id)
    mensaje.delete()
    return redirect('admin_mensajes')
