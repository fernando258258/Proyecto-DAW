from django.core.management.base import BaseCommand
from tienda.models import Producto

class Command(BaseCommand):
    help = 'Carga los 8 productos del catálogo'

    def handle(self, *args, **kwargs):
        productos = [
            {'nombre': 'Espresso Intenso', 'formato': 'capsulas', 'descripcion': 'Cápsula compatible · int. 11', 'precio': 60, 'stock': 120},
            {'nombre': 'Decaf Suave', 'formato': 'capsulas', 'descripcion': 'Cápsula descafeinada · int. 6', 'precio': 60, 'stock': 80},
            {'nombre': 'Lungo Dorado', 'formato': 'capsulas', 'descripcion': 'Cápsula compatible · int. 6', 'precio': 70, 'stock': 45},
            {'nombre': 'Mezcla de la Casa', 'formato': 'bolsitas', 'descripcion': 'Grano entero · 250 g', 'precio': 80, 'stock': 60},
            {'nombre': 'Origen Colombia', 'formato': 'bolsitas', 'descripcion': 'Grano molido · 250 g', 'precio': 90, 'stock': 50},
            {'nombre': 'Tueste Oscuro', 'formato': 'bolsitas', 'descripcion': 'Grano entero · 500 g', 'precio': 140, 'stock': 30},
            {'nombre': 'Soluble Premium', 'formato': 'tarros', 'descripcion': 'Tarro de vidrio · 200 g', 'precio': 70, 'stock': 35},
            {'nombre': 'Clásico Cafital', 'formato': 'tarros', 'descripcion': 'Tarro de vidrio · 300 g', 'precio': 100, 'stock': 40},
        ]

        for p in productos:
            Producto.objects.create(**p)
            self.stdout.write(self.style.SUCCESS(f"Creado: {p['nombre']}"))

        self.stdout.write(self.style.SUCCESS('¡8 productos cargados!'))