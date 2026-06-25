# Documentación CSS - Metodología BEM

## Estructura General

Este archivo CSS sigue la **metodología BEM (Block Element Modifier)** para mantener el código organizado y fácil de entender. La estructura está documentada con comentarios en cada clase.

---

##  Nomenclatura BEM

- **BLOCK**: Componente independiente y reutilizable (ej: `.navbar`, `.hero`, `.category-grid`)
- **ELEMENT**: Parte de un bloque, identificada con `__` (ej: `.navbar__logo`, `.card__image`)
- **MODIFIER**: Variación de un bloque o elemento, identificada con `--` o `-` (ej: `.btn--primary`, `.card--active`)

**Nota:** En este proyecto usamos guiones `-` en lugar de `__` para los elementos por convención del equipo.

---

##  Bloques Principales

### 1. **Navegación (.navbar)**
- `.navbar` - Contenedor principal de la barra de navegación
- `.nav-container` - Distribuye logo y menú horizontalmente
- `.brand` - Logo del sitio con imagen de fondo
- `.brand-text` - Texto "Cafital" junto al logo
- `.nav-menu` - Menú de navegación
- `.nav-menu a` - Enlaces del menú

### 2. **Secciones (.section)**
- `.section` - Sección genérica con padding
- `.section-intro-band` - Sección con fondo café oscuro
- `.section-intro` - Grilla de 3 características
- `.intro-item` - Cada característica individual

### 3. **Tipografía**
- `.section-tag` - Etiqueta roja pequeña sobre títulos
- `.section-title` - Título principal de sección
- `.accent` - Modificador para texto en rojo

### 4. **Botones (.btn)**
- `.btn` - Botón base
- `.btn-primary` - Botón rojo principal con hover invertido
- `.btn-small` - Botón pequeño para tarjetas

### 5. **Hero Section (.hero)**
- `.hero` - Contenedor con imagen y texto lado a lado
- `.hero-content` - Contenido de texto
- `.hero-image` - Contenedor de imagen
- `.hero-image-placeholder` - Imagen de fondo

### 6. **Tarjetas de Categorías (.category-grid)**
- `.category-grid` - Grilla de 3 columnas
- `.category-card` - Tarjeta individual con hover
- `.card-image` - Área de imagen
- `.card-image-capsulas` - Imagen de cápsulas
- `.card-image-bolsitas` - Imagen de bolsitas
- `.card-image-tarros` - Imagen de tarros
- `.card-image-label` - Etiqueta sobre imagen
- `.card-content` - Contenido de texto
- `.card-link` - Enlace de exploración

### 7. **Catálogo de Productos**
- `.filters` - Botones de filtro
- `.filter-btn` - Botón individual de filtro
- `.format-heading` - Título de formato
- `.product-grid` - Grilla de productos
- `.product-card` - Tarjeta de producto
- `.product-image` - Imagen del producto
- `.product-info` - Información del producto
- `.product-format-tag` - Etiqueta de formato
- `.product-footer` - Precio y botón de agregar
- `.product-price` - Precio del producto

### 8. **Contacto (.contact-layout)**
- `.contact-layout` - Contenedor formulario + info
- `.contact-form-card` - Tarjeta con formulario
- `.contact-info-card` - Tarjeta con información
- `.form-group` - Grupo de campo
- `.contact-info-item` - Línea de información
- `.social-links` - Enlaces a redes sociales

### 9. **Página Sobre Nosotros**
- `.about-hero` - Sección de imagen + texto
- `.about-image` - Imagen de sección
- `.about-text` - Texto de sección
- `.about-title` - Título principal
- `.values-grid` - Grilla de valores
- `.value-card` - Tarjeta individual de valor
- `.value-icon` - Ícono emoji de valor

### 10. **Footer (.site-footer)**
- `.site-footer` - Contenedor principal
- `.footer-grid` - Grilla de 4 columnas
- `.footer-logo` - Logo con imagen de fondo (versión roja)
- `.footer-bottom` - Línea de copyright

---

##  Responsive Design

Las media queries están documentadas al final del archivo CSS.

**Breakpoint:** `max-width: 768px` (tablets y móviles)

Cambios principales:
- Layouts flex pasan de lado-a-lado a vertical
- Grillas pasan de múltiples columnas a una sola
- Menú se apila verticalmente

---

##  Variables de Color

```css
--color-cafe: #3d2b1f;     /* Marrón oscuro principal */
--color-piel: #f2e8dc;     /* Beige claro fondo */
--color-rojo: #e94f4f;     /* Rojo para acentos y botones */
```

---

##  Variables de Tipografía

```css
--font-primary: 'Fraunces', serif;      /* Títulos */
--font-secondary: 'Open Sans', sans-serif; /* Cuerpo */
```

---

##  Cómo Usar

1. **Para agregar una nueva clase**, mantén la estructura BEM
2. **Agrupa clases relacionadas** bajo comentarios de bloque
3. **Documenta cada clase** con su propósito
4. **Usa variables** para colores y tipografía consistentes

---

##  Ejemplo de Nueva Clase

```css
/* ELEMENT: .example-component
   Descripción breve de qué hace esta clase */
.example-component {
  /* tu CSS aquí */
}
```

---

**Última actualización:** 2026-06-24  
**Metodología:** BEM (Block Element Modifier)
