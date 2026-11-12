// Introducción a JavaScript ECMAScript 6
// Curso de JavaScript y React · María Celeste Guevara

// 1. Variables let y scope
let peliculaTitulo = "Avengers"; // scope global

function setTitulo() {
  let peliculaTitulo = "Terminator 2"; // scope local
  console.log(peliculaTitulo);
  // let peliculaTitulo = "Avengers"; // error: ya fue declarada en este bloque
}

setTitulo();
console.log(peliculaTitulo);

// 2. Constantes const
const peliculaPrecio = 20; // global

function setPrecio() {
  const peliculaPrecio = 50; // local
  console.log(peliculaPrecio);
  // peliculaPrecio = 60; // error: no se puede asignar otro valor a una constante
}

setPrecio();
console.log(peliculaPrecio);

// 3. Concatenar con backticks (versión con function, comentada)
/*
function mostrarPrecio() {
  let peliculaPrecio = 65;
  console.log("El precio es: " + peliculaPrecio);
  console.log(`El precio es: ${peliculaPrecio}`);
}
*/

// 4. La misma función escrita como arrow function
const mostrarPrecio = () => {
  let peliculaPrecio = 70;
  console.log(`El precio es: ${peliculaPrecio}`);
};

mostrarPrecio();

// 5. Recorrer un array con map
let peliculas = [
  { idPelicula: 1, titulo: "Avatar" },
  { idPelicula: 2, titulo: "Terminator 2" },
  { idPelicula: 3, titulo: "Silent Hill" },
];

const mostrarTodas = (peliculas) => {
  peliculas.map((p) => console.log(p.idPelicula, p.titulo));
};

mostrarTodas(peliculas);
