# -*- coding: utf-8 -*-
"""Contenido del documento paso a paso. Lo usa generar.py para crear el PDF y el Word.

Bloques:
  ("parte", kicker, titulo, intro)   ("paso", titulo)   ("p", texto)
  ("ol", [items])   ("ul", [items])   ("code", nombre, texto)
  ("img", archivo, pie)   ("nota", tipo, titulo, texto)   tipo: info | hoy | error
Marcado en línea: **negrita** y `código`.
"""

TITULO = "Curso de JavaScript (ES6) y React"
SUBTITULO = "Documentación paso a paso con capturas"
CURSO = "Curso gratuito de JavaScript y React · Mariano Puglisi y Fernando Bursa"
AUTORA = "María Celeste Guevara"
CARNET = "2211401"
FECHA = "12 de noviembre de 2026"
REPO = "https://github.com/Celestegvr/curso-javascript-react"
SITIO = "https://curso-javascript-react.vercel.app"

INTRO = [
    ("p", "Este documento recoge, paso a paso, lo que se explica en las primeras secciones del curso: la instalación de las herramientas, una introducción a JavaScript ECMAScript 6 y la creación del primer componente en React. Seguí cada clase en mi equipo; las capturas muestran mi código, mi terminal y mi navegador, no el video."),
    ("p", "El código terminado está en GitHub y publicado en Vercel (ver el paso 16):"),
    ("ul", [f"Repositorio: `{REPO}`", f"App React: `{SITIO}`", f"Mini proyecto ES6: `{SITIO}/introjs/`"]),
    ("nota", "info", "Sobre las rutas", "En el video las carpetas se crean en la raíz del disco (`C:\\introjs` y `C:\\demoreact`). Yo las creé dentro de `Desktop\\IA\\curso-javascript-react` para tener todo el trabajo en un solo repositorio; los comandos son los mismos."),
]

BLOQUES = [
    # ---------------- PARTE 1 ----------------
    ("parte", "Parte 1", "Instalación de herramientas", "Se prepara el entorno: un editor de código con extensiones útiles y Node.js para trabajar con React."),

    ("paso", "Instalar Visual Studio Code"),
    ("p", "VS Code es uno de los editores más usados. Trae **IntelliSense** (autocompletado), herramientas de **depuración** y una **terminal integrada**."),
    ("ol", [
        "Buscar `vs code` en Google y entrar a la página oficial: `code.visualstudio.com`.",
        "Hacer clic en **Download** y elegir el instalador del sistema. En el curso se descarga el de **Windows de 64 bits**.",
        "Abrir el archivo descargado, **aceptar los términos** y pulsar **Siguiente**.",
        "Dejar la **ruta de instalación por defecto** y el grupo de programas sugerido.",
        "En las tareas adicionales marcar **Crear un icono en el escritorio** y **Agregar «Abrir con Code»** al menú contextual del Explorador de Windows.",
        "Pulsar **Instalar** y, al terminar, **Finalizar**. El editor se abre solo.",
    ]),
    ("p", "Para comprobar que quedó instalado (junto con Node.js, del paso 5) se pueden pedir las versiones desde la consola:"),
    ("img", "01-05-versiones.png", "Versiones instaladas en mi equipo: VS Code, Node.js y npm."),

    ("paso", "Tener a mano los atajos de teclado"),
    ("p", "La clase incluye un PDF con todos los atajos de VS Code (también está en el menú **Help → Keyboard Shortcuts Reference**). Los que se usan en el curso son:"),
    ("ul", [
        "**Ctrl + S**: guardar el archivo (con Prettier configurado, también lo formatea).",
        "**Ctrl + Ñ** (teclado español) o **Ctrl + `** (teclado inglés): abrir la terminal integrada.",
        "**Ctrl + rueda del ratón**: agrandar la letra en la consola de Windows.",
        "**F5** en el navegador: recargar la página. **F12**: abrir las herramientas de desarrollo y la consola.",
    ]),

    ("paso", "Instalar las extensiones de VS Code"),
    ("ol", [
        "Abrir la vista de **Extensiones**: el icono de los cuadrados en la barra lateral (o **Ctrl + Shift + X**).",
        "Buscar `Prettier` e instalar **Prettier - Code formatter**. Ordena la indentación y la estructura del código.",
        "Buscar `Bracket Pair Colorizer` e instalar la versión **2**. Colorea cada par de llaves para ver dónde empieza y termina cada función.",
        "Buscar `ES7` e instalar **ES7+ React/Redux/React-Native snippets**. Con una abreviatura escribe bloques de código completos (componentes, imports, etc.).",
    ]),
    ("p", "Las mismas extensiones también se pueden instalar desde la consola con `code --install-extension`. Así las instalé y luego comprobé la lista:"),
    ("img", "03-extensiones.png", "Instalación de las tres extensiones del curso y lista de extensiones de mi VS Code."),
    ("nota", "hoy", "Nota actual", "Bracket Pair Colorizer 2 está obsoleta: desde 2021 VS Code colorea los pares de llaves por sí solo (ajuste `editor.bracketPairColorization.enabled`). Todavía se puede instalar, pero no es necesaria."),

    ("paso", "Configurar Prettier para que formatee al guardar"),
    ("ol", [
        "Ir a **File → Preferences → Settings** (o **Ctrl + ,**).",
        "Escribir `format` en el buscador de ajustes.",
        "En **Editor: Default Formatter** elegir **Prettier - Code formatter**.",
        "Marcar **Editor: Format On Save**.",
        "Cerrar los ajustes. Cada vez que se guarda con **Ctrl + S** el archivo se formatea solo.",
    ]),
    ("p", "Esos dos ajustes quedan escritos en un archivo `settings.json`. Yo los guardé solo para este proyecto, en `.vscode/settings.json`, para no cambiar el formato de mis otros proyectos:"),
    ("img", "04-settings-json.png", "Ajustes de Prettier en .vscode/settings.json."),

    ("paso", "Instalar Node.js"),
    ("p", "Node.js hace falta para crear el proyecto React e instalar sus módulos con `npm`."),
    ("ol", [
        "Buscar `Node` y entrar a la página oficial: `nodejs.org`.",
        "Descargar la versión **LTS** (soporte a largo plazo): es la estable y probada. La otra, «Current», trae lo más nuevo, pero se recomienda la LTS.",
        "Ejecutar el instalador: **Next**, aceptar los términos, dejar la ruta y las opciones por defecto e **Install**.",
        "Aceptar la ventana de seguridad de Windows y pulsar **Finish**.",
        "Comprobar en una consola nueva con `node -v` y `npm -v` (ver la figura del paso 1).",
    ]),
    ("nota", "hoy", "Nota actual", "En el video se instala Node 14.17.4 LTS. En mi equipo está la versión 24.20.0; lo importante es elegir siempre la que dice LTS."),

    # ---------------- PARTE 2 ----------------
    ("parte", "Parte 2", "Introducción a JavaScript ECMAScript 6", "Un mini proyecto para repasar las novedades de ES6 que después se usan en React. Todos los ejemplos se escriben en `script.js` y el resultado se ve en la consola del navegador (F12)."),

    ("paso", "Crear el mini proyecto «introjs» y verlo en el navegador"),
    ("p", "**a) Crear la carpeta y los archivos desde la consola.** En la lupa de Windows escribir `CMD` y pulsar Enter."),
    ("ol", [
        "Ir a la carpeta donde se guardará el proyecto (en el video, `cd \\` lleva a la raíz del disco C:).",
        "`mkdir introjs` crea la carpeta y `cd introjs` entra en ella.",
        "`copy con index.html` crea el archivo. Se termina con **Ctrl + Z** y **Enter**. Repetir con `script.js`.",
        "`code .` abre VS Code en esa carpeta. Si pregunta si se confía en los autores, pulsar **Yes**.",
    ]),
    ("img", "06-crear-introjs.png", "Creación de la carpeta introjs y de sus dos archivos desde la consola."),
    ("p", "**b) Escribir la estructura HTML.** En `index.html` escribir `html` y elegir el snippet **html:5** (o `!` y Tab). Cambiar el título a «Intro», agregar un `h1` y enlazar el script con `type=\"module\"` (prepara el archivo para `import` y `export`). El `./` indica que `script.js` está en la misma carpeta."),
    ("img", "06-index-html.png", "index.html del mini proyecto."),
    ("p", "**c) Abrirlo con un servidor web.** Un script con `type=\"module\"` no funciona abriendo el archivo con doble clic. En el curso se usa Internet Information Services (IIS):"),
    ("ol", [
        "Buscar **«Activar o desactivar las características de Windows»**, marcar **Internet Information Services** y pulsar **Aceptar**.",
        "Abrir el **Administrador de IIS** (buscar `IIS` en la lupa).",
        "En **Sitios**, clic derecho sobre **Default Web Site** → **Agregar directorio virtual**. Alias: `introjs`. Ruta física: la carpeta del proyecto.",
        "Abrir `http://localhost/introjs/index.html` en Chrome. El nombre del archivo es opcional porque `index.html` se abre por defecto.",
    ]),
    ("nota", "info", "Lo que hice yo", "No activé IIS en mi equipo. Usé un servidor local equivalente (la extensión Live Server de VS Code o `python -m http.server` hacen lo mismo), por eso en las capturas la dirección es `localhost:5530/introjs/`. El resultado es idéntico."),

    ("paso", "Declarar variables con let y entender el scope"),
    ("p", "`let` declara una variable cuyo valor **puede cambiar**. Los nombres se escriben en **camelCase**: la primera palabra en minúscula y la inicial de las siguientes en mayúscula (`peliculaTitulo`)."),
    ("ol", ["Crear la función `setTitulo` con una variable `let`, mostrarla con `console.log`, llamar a la función, guardar y recargar con F5."]),
    ("img", "07-let-codigo.png", "Primera versión de script.js."),
    ("img", "07-let-consola.png", "La consola muestra «Terminator 2»."),
    ("ol", ["Probar a declarar otra vez la misma variable dentro de la función. VS Code la subraya y el navegador muestra un error: **una variable let no se puede volver a declarar en el mismo bloque**."]),
    ("img", "07-let-error-codigo.png", "VS Code marca la segunda declaración."),
    ("img", "07-let-error-consola.png", "Error en la consola: la variable ya fue declarada."),
    ("ol", ["Comentar esa línea y declarar una variable **con el mismo nombre fuera de la función**. Mostrarla después de llamar a la función."]),
    ("img", "07-scope-codigo.png", "Variable global y variable local con el mismo nombre."),
    ("img", "07-scope-consola.png", "Se imprimen las dos películas."),
    ("p", "Se ven los dos títulos por el **scope** (alcance) de cada variable: la de afuera es **global** y se puede usar en todo el archivo; la de adentro es **local**, solo existe dentro de `setTitulo` y ahí tapa a la global."),

    ("paso", "Declarar constantes con const"),
    ("ol", [
        "Crear la función `setPrecio` con `const peliculaPrecio = 50`, mostrarla y llamar a la función.",
        "Probar a asignarle otro valor (`peliculaPrecio = 60;`). Aparece un error: **a una constante no se le puede cambiar el valor**.",
    ]),
    ("img", "08-const-error-consola.png", "TypeError: asignación a una variable constante."),
    ("ol", ["Comentar esa línea. Declarar una constante global con el mismo nombre (valor 20) y mostrarla al final. El scope funciona igual que con let."]),
    ("img", "08-const-codigo.png", "Constante global y constante local."),
    ("img", "08-const-consola.png", "Se imprimen 50 (local) y 20 (global)."),
    ("nota", "info", "¿Cuándo usar const?", "Para datos que no cambian mientras la aplicación está en uso, por ejemplo el correo del usuario que inició sesión."),

    ("paso", "Concatenar texto con backticks"),
    ("ol", [
        "Crear la función `mostrarPrecio` y concatenar con `+`, la forma clásica: `\"El precio es: \" + peliculaPrecio`.",
        "Escribir lo mismo con **backticks**: todo el texto entre `` ` `` y cada variable dentro de `${ }`. Ya no hace falta un `+` por cada variable.",
    ]),
    ("img", "09-backticks-codigo.png", "Las dos formas de concatenar."),
    ("img", "09-backticks-consola.png", "Las dos líneas dan el mismo resultado."),
    ("nota", "info", "¿Dónde está el backtick?", "En el teclado español suele estar junto a la tecla de los corchetes y llaves. Si no aparece: Alt + 96 en el teclado numérico."),

    ("paso", "Escribir funciones flecha (arrow functions)"),
    ("ol", [
        "Comentar la función anterior con `/* ... */`.",
        "Declararla como constante: `const mostrarPrecio = () => { ... };`",
        "Llamarla como cualquier función y recargar el navegador.",
    ]),
    ("img", "10-arrow-codigo.png", "mostrarPrecio escrita como función flecha."),
    ("ul", [
        "Entre los paréntesis van los **parámetros**. Si hay **uno solo**, se pueden omitir los paréntesis.",
        "Si el cuerpo es **una sola instrucción**, se pueden omitir las llaves. Con varias instrucciones son obligatorias.",
    ]),

    ("paso", "Recorrer un array con map"),
    ("p", "`map` está disponible en todos los arrays: recorre cada elemento como un bucle y ejecuta una función por cada uno."),
    ("ol", [
        "Definir el array `peliculas`: los corchetes crean el array y cada par de llaves es un objeto con `idPelicula` y `titulo`. Los números van sin comillas y los textos entre comillas.",
        "Crear la función flecha `mostrarTodas`, que recibe el array como parámetro.",
        "Dentro, llamar a `peliculas.map()` con una función flecha que recibe cada elemento (`p`) y lo imprime.",
        "Llamar a `mostrarTodas(peliculas)`, guardar y recargar.",
    ]),
    ("img", "11-map-codigo.png", "Array de películas recorrido con map."),
    ("img", "11-final-consola.png", "Consola con el script.js completo: todos los ejemplos de la Parte 2."),
    ("nota", "info", "Por qué conviene", "La función flecha dentro de map no necesita nombre ni declararse aparte: recibe el elemento y lo usa ahí mismo. La estructura se parece a JSON, pero es un objeto de JavaScript."),

    # ---------------- PARTE 3 ----------------
    ("parte", "Parte 3", "Primeros pasos con React", "Se crea el proyecto `peliculas_spa` (Single Page Application) y su primer componente funcional."),

    ("paso", "Entender qué es React"),
    ("ul", [
        "Es una **librería de JavaScript para construir interfaces de usuario** (front end), creada por Facebook. Su documentación oficial está en `react.dev`.",
        "Usa las novedades de ECMAScript más herramientas propias: **componentes**, **hooks** de estado, de contexto y de referencia, y componentes de terceros. Modificar el DOM a mano con JavaScript es tedioso; React lo simplifica.",
        "El curso trabaja con **componentes funcionales**.",
    ]),

    ("paso", "Crear el proyecto React"),
    ("ol", [
        "Abrir `CMD` y entrar a la carpeta de trabajo (en el video: `cd \\`, `mkdir demoreact` y `cd demoreact`).",
        "Ejecutar `npx create-react-app peliculas_spa`. Tarda unos minutos (en mi equipo, unos 8).",
        "Entrar con `cd peliculas_spa` y abrir el proyecto con `code .`. Confiar en los autores (**Yes**).",
    ]),
    ("img", "13-create-react-app.png", "Creación del proyecto peliculas_spa."),
    ("nota", "hoy", "Nota actual", "Create React App fue declarado obsoleto en 2025 y lo avisa al empezar (línea amarilla), pero sigue funcionando: instaló React 19 y el proyecto compila bien. Una alternativa actual es Vite: `npm create vite@latest`."),

    ("paso", "Ejecutar la app y entender cómo funciona"),
    ("ol", ["Abrir la terminal de VS Code (**Ctrl + Ñ**) y ejecutar `npm start`. Se abre el navegador en `http://localhost:3000`."]),
    ("img", "14-npm-start.png", "El servidor de desarrollo compila sin errores."),
    ("img", "14-react-inicio.png", "Página inicial estándar de un proyecto React."),
    ("p", "El recorrido que hace la aplicación para mostrar esa página:"),
    ("ol", [
        "`public/index.html` tiene un `div` vacío con `id=\"root\"`.",
        "`src/index.js` importa los componentes y los dibuja dentro de `root` con `render`. `React.StrictMode` viene por defecto y activa el modo estricto.",
        "`src/App.js` es el componente que retorna el HTML de la página: el logo, el texto y el enlace. Para usarlo se escribe como etiqueta: `<App />`, y al importarlo no hace falta la extensión `.js`.",
    ]),
    ("img", "14-public-index-html.png", "El div root en public/index.html."),
    ("img", "14-index-js-original.png", "src/index.js tal como lo crea create-react-app."),
    ("img", "14-app-js.png", "src/App.js: el componente de la página inicial."),
    ("nota", "hoy", "Diferencia con el video", "En el video `index.js` usa la forma de React 17: `ReactDOM.render(<App />, document.getElementById(\"root\"))`. Mi proyecto trae React 19, que usa `ReactDOM.createRoot(...)` y `root.render(...)`. La idea es la misma."),
    ("ol", ["Quitar el logo en `App.js` y guardar: el navegador se actualiza solo, sin F5. Después dejar el archivo como estaba."]),
    ("img", "14-react-sin-logo.png", "Al guardar App.js sin el logo, la página se actualiza sola."),
    ("p", "Todo lo que se escribe en React termina convertido en JavaScript, el lenguaje que entienden todos los navegadores."),

    ("paso", "Crear el primer componente: Peliculas"),
    ("p", "**a) Limpiar el proyecto.** En `src` borrar `App.css`, `App.js`, `App.test.js`, `index.css`, `logo.svg`, `reportWebVitals.js` y `setupTests.js`. En `index.js` borrar sus `import`, el componente `<App />` y la llamada a `reportWebVitals`."),
    ("p", "**b) Crear el componente.** Clic derecho en `src` → **New Folder** → `components`; dentro, la carpeta `Pelicula` y el archivo `Peliculas.jsx` (las extensiones .js y .jsx son válidas; .jsx ayuda al editor a reconocer el componente)."),
    ("img", "15-peliculas-v1.png", "Primer componente funcional y estructura del proyecto tras la limpieza."),
    ("ul", [
        "**Imports arriba**: todo componente importa React con `import React from \"react\";`.",
        "**Definición**: una función flecha cuyo nombre empieza con **mayúscula**, para que React la reconozca como componente. Es un *componente funcional*; los de clase existen, pero el curso no los usa.",
        "**return**: devuelve el HTML (JSX) que el componente insertará donde se use.",
        "**export default**: sin exportarlo, ningún otro archivo puede importarlo.",
    ]),
    ("p", "**c) Mostrarlo en index.js.** Importarlo con la ruta relativa, sin extensión, y escribirlo como etiqueta con la P mayúscula, igual que se exportó:"),
    ("img", "15-index-js-final.png", "index.js final: importa y muestra Peliculas."),
    ("img", "15-react-peliculas-v1.png", "El navegador muestra el componente."),
    ("p", "**d) Un único elemento padre.** Si se agrega un segundo `div` al mismo nivel, aparece un error en VS Code y en el navegador:"),
    ("img", "15-error-padre-codigo.png", "VS Code marca el segundo div."),
    ("img", "15-error-padre-navegador.png", "Error de compilación: los elementos JSX deben estar dentro de una sola etiqueta."),
    ("p", "Se soluciona envolviendo todo en un **Fragment**, una etiqueta vacía `<> </>`:"),
    ("img", "15-fragment-codigo.png", "Peliculas.jsx con Fragment."),
    ("img", "15-react-final.png", "Resultado final del componente."),
    ("p", "**e) Virtual DOM y Webpack.** Lo que va dentro del `return` parece HTML, pero es JSX. El **Virtual DOM** lo procesa y genera el HTML final dentro de un archivo JavaScript. Por eso el JSX es **estricto**: toda etiqueta debe cerrarse. **Webpack** compila los componentes y avisa si algo está mal; por ejemplo, al quitar el cierre de un `div`:"),
    ("img", "15-error-sin-cerrar-navegador.png", "Error de compilación por una etiqueta sin cerrar (JSX incompleto)."),

    # ---------------- PUBLICACIÓN ----------------
    ("parte", "Publicación", "Código en GitHub y Vercel", "El código de los dos proyectos se subió a GitHub y se publicó en Vercel."),

    ("paso", "Compilar y publicar el código"),
    ("ol", [
        "Comprobar que la app compila para producción con `npm run build`.",
        "Subir la carpeta del curso a GitHub: `" + REPO + "`.",
        "En Vercel, **Add New → Project**, importar el repositorio y pulsar **Deploy**. El archivo `vercel.json` le indica cómo compilar `peliculas_spa` y copia `introjs` dentro del sitio.",
        "Cada vez que se sube un cambio a la rama `main`, Vercel vuelve a publicar el sitio.",
    ]),
    ("img", "16-npm-run-build.png", "Compilación de producción sin errores."),
    ("code", "vercel.json", '{\n  "installCommand": "cd peliculas_spa && npm install",\n  "buildCommand": "cd peliculas_spa && npm run build && cp -r ../introjs build/introjs",\n  "outputDirectory": "peliculas_spa/build"\n}'),
    ("img", "16-vercel-react.png", f"App React publicada en {SITIO}"),
    ("img", "16-vercel-introjs.png", f"Mini proyecto publicado en {SITIO}/introjs/"),
]

CIERRE = [
    ("p", "Al terminar estos pasos quedaron:"),
    ("ul", [
        "VS Code con Prettier (formato al guardar), Bracket Pair Colorizer 2 y los snippets de React; Node.js LTS instalado.",
        "El mini proyecto `introjs` con ejemplos de let, const, scope, backticks, funciones flecha y map.",
        "El proyecto React `peliculas_spa` con su primer componente funcional, `Peliculas`.",
        f"Todo el código en GitHub ({REPO}) y publicado en Vercel ({SITIO}).",
    ]),
]
