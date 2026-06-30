from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('productos/', views.productos, name='productos'),
    path('sobre-nosotros/', views.sobre_nosotros, name='sobre_nosotros'),
    path('contacto/', views.contacto, name='contacto'),
    path('registro/', views.registro, name='registro'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('carrito/agregar/<int:producto_id>/', views.agregar_carrito, name='agregar_carrito'),
    path('carrito/', views.carrito, name='carrito'),
    path('carrito/eliminar/<int:item_id>/', views.eliminar_carrito, name='eliminar_carrito'),
    path('carrito/confirmar/', views.confirmar_pedido, name='confirmar_pedido'),
    path('panel/productos/', views.admin_productos, name='admin_productos'),
    path('panel/pedidos/', views.admin_pedidos, name='admin_pedidos'),
    path('panel/mensajes/', views.admin_mensajes, name='admin_mensajes'),
    path('panel/mensajes/leido/<int:mensaje_id>/', views.marcar_leido, name='marcar_leido'),
]