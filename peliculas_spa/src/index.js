import React from "react";
import ReactDOM from "react-dom/client";
import Peliculas from "./components/Pelicula/Peliculas";

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  <React.StrictMode>
    <Peliculas />
  </React.StrictMode>
);
