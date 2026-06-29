const productosPorCategoria = {
  capsulas: [
    {
      nombre: "Espresso Intenso",
      precio: "Bs. 60",
      descripcion: "Cápsula compatible, intensidad 11.",
      imagen: "https://res.cloudinary.com/dk0my05zq/image/upload/v1782308386/index-capsulas_biqowj.jpg",
    },
    {
      nombre: "Decaf Suave",
      precio: "Bs. 60",
      descripcion: "Cápsula descafeinada, intensidad 6.",
      imagen: "https://res.cloudinary.com/dk0my05zq/image/upload/v1782308386/index-capsulas_biqowj.jpg",
    },
    {
      nombre: "Lungo Dorado",
      precio: "Bs. 70",
      descripcion: "Cápsula compatible, intensidad 6.",
      imagen: "https://res.cloudinary.com/dk0my05zq/image/upload/v1782619189/prodcuto-capsula-3_dbkdzm.jpg",
    },
  ],
  bolsitas: [
    {
      nombre: "Mezcla de la Casa",
      precio: "Bs. 80",
      descripcion: "Grano entero, bolsa de 250 g.",
      imagen: "https://res.cloudinary.com/dk0my05zq/image/upload/v1782318168/index-bolsas_rhn8wo.jpg",
    },
    {
      nombre: "Origen Colombia",
      precio: "Bs. 90",
      descripcion: "Grano molido, bolsa de 250 g.",
      imagen: "https://res.cloudinary.com/dk0my05zq/image/upload/v1782318168/index-bolsas_rhn8wo.jpg",
    },
    {
      nombre: "Tueste Oscuro",
      precio: "Bs. 140",
      descripcion: "Grano entero, bolsa de 500 g.",
      imagen: "https://res.cloudinary.com/dk0my05zq/image/upload/v1782318168/index-bolsas_rhn8wo.jpg",
    },
  ],
  tarros: [
    {
      nombre: "Soluble Premium",
      precio: "Bs. 70",
      descripcion: "Tarro de vidrio, 200 g.",
      imagen: "https://res.cloudinary.com/dk0my05zq/image/upload/v1782319280/index-tarros_op67tw.png",
    },
    {
      nombre: "Clásico Cafital",
      precio: "Bs. 100",
      descripcion: "Tarro de vidrio, 300 g.",
      imagen: "https://res.cloudinary.com/dk0my05zq/image/upload/v1782319280/index-tarros_op67tw.png",
    },
  ],
};

function crearTarjetaProducto(producto, etiqueta) {
  const tarjeta = document.createElement("article");
  tarjeta.className = "product-card";

  tarjeta.innerHTML = `
    <div class="product-image" style="background-image: url('${producto.imagen}')"></div>
    <div class="product-info">
      <span class="product-format-tag">${etiqueta}</span>
      <h3>${producto.nombre}</h3>
      <p>${producto.descripcion}</p>
      <div class="product-footer">
        <span class="product-price">${producto.precio}</span>
        <a href="#" class="btn btn-primary btn-small">Agregar</a>
      </div>
    </div>
  `;

  return tarjeta;
}

function renderProductos(contenedorId, etiqueta, productos) {
  const contenedor = document.getElementById(contenedorId);

  if (!contenedor) {
    return;
  }

  productos.forEach((producto) => {
    contenedor.appendChild(crearTarjetaProducto(producto, etiqueta));
  });
}

document.addEventListener("DOMContentLoaded", () => {
  renderProductos("capsulas-grid", "Cápsulas", productosPorCategoria.capsulas);
  renderProductos("bolsitas-grid", "Bolsitas", productosPorCategoria.bolsitas);
  renderProductos("tarros-grid", "Tarros", productosPorCategoria.tarros);
});