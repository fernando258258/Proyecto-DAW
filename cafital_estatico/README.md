# Cafital - Cafetería de Especialidad & Panel de Administración

Este es el prototipo frontend estático de **Cafital**, una tienda en línea y panel de gestión para una marca de café tostado artesanal. El proyecto ha sido desarrollado utilizando HTML5 semántico y CSS3 moderno (siguiendo la metodología BEM y un sistema de diseño premium).

Este repositorio sirve como base de diseño y maqueta estática para la posterior integración del backend.

---

##  Estructura del Proyecto

```text
cafital_estatico/
├── index.html                  # Página de inicio (Hero, propuesta de valor, categorías)
├── sobre-nosotros.html         # Historia, filosofía y valores de la marca
├── productos.html              # Catálogo de productos con filtros interactivos
├── contacto.html               # Formulario de contacto y datos de sucursales
├── admin.html                  # Panel Admin: Gestión del catálogo de productos
├── admin-pedidos.html          # Panel Admin: Bandeja de pedidos de clientes
├── admin-mensajes.html         # Panel Admin: Bandeja de mensajes del formulario
├── css/
│   ├── style.css               # Estilos del sitio web público
│   ├── admin.css               # Estilos del panel de administración (BEM, variables)
│   └── README.md               # Documentación interna de la arquitectura CSS
```

---

##  Tecnologías y Recursos Utilizados

*   **HTML5 Semántico:** Uso estructurado de etiquetas como `<header>`, `<main>`, `<aside>`, `<section>`, `<article>` y `<footer>` para mejor SEO y accesibilidad.
*   **CSS3 Moderno:** 
    *   Variables CSS para un sistema de diseño consistente (colores, tipografía, sombras, transiciones).
    *   Metodología BEM (adaptada) para modularidad de clases.
    *   Diseño fluido y 100% responsivo con CSS Grid y Flexbox.
*   **Fuentes de Google Fonts:**
    *   *Fraunces* (Serif elegante para títulos y marca).
    *   *Open Sans* (Sans-serif limpia para cuerpo de texto y panel de administración).
*   **Iconos:**
    *   **Flaticon Uicons (via CDN):** Combinación de estilos *Regular Rounded* (`fi-rr-`), *Thin Rounded* (`fi-tr-`) y *Thin Straight* (`fi-ts-`) para una interfaz moderna y consistente.

---

##  Secciones del Panel de Administración

El panel de administración cuenta con tres secciones clave completamente maquetadas:

1.  **Productos (`admin.html`):** Vista de catálogo con tabla de stock, precios y formato del producto. Incluye botones rápidos para **Editar** y **Eliminar**.
2.  **Pedidos (`admin-pedidos.html`):** Tabla detallada de las compras de clientes con estados dinámicos controlados por Badges visuales (Pendiente, Enviado, Entregado, Cancelado).
3.  **Mensajes (`admin-mensajes.html`):** Bandeja de entrada que recopila las consultas de los clientes. Permite responder directamente por correo (`mailto:`) o eliminar el mensaje.

---

##  Guía de Integración para el Backend

Para el desarrollador encargado de implementar el backend (base de datos y lógica del lado del servidor):

### 1. Dinamización de Tablas
Cada tabla de administración cuenta con filas de prueba (`<tr>`) comentadas en el HTML. Se debe reemplazar esta estructura por un bucle (`foreach`/`map`) que recorra los datos reales de la base de datos.

### 2. Acciones (Botones del Lápiz y Basura)
Actualmente, los botones de acción apuntan a `href="#"`. 
*   **Editar:** Debe modificarse para redirigir al formulario de edición correspondiente pasando el ID del elemento (ej. `editar-producto.php?id=ID` o una ruta como `/admin/productos/editar/:id`), o abrir un modal que cargue los datos por AJAX.
*   **Eliminar:** Debe enlazarse a un controlador o función de JavaScript que solicite confirmación al usuario antes de enviar la petición de borrado (POST/DELETE) al servidor.

### 3. Gestión de Badges de Estado
Las clases de CSS para los estados de pedidos y mensajes ya están definidas. Solo debes imprimir la clase adecuada según el estado del registro:
*   `badge-pendiente` / `badge-sin-leer` (Naranja/Crema)
*   `badge-enviado` / `badge-respondido` (Azul/Celeste)
*   `badge-entregado` / `badge-leido` (Verde/Verde Claro)
*   `badge-cancelado` (Rojo/Rosa)

---

##  Cómo Ejecutar Localmente

1. Clona el repositorio.
2. Abre la carpeta del proyecto en tu editor preferido (se recomienda VS Code).
3. Si usas VS Code, haz clic derecho sobre `index.html` y selecciona **Open with Live Server**.
4. Para acceder directamente al panel de administración, navega a `http://localhost:5500/admin.html`.
