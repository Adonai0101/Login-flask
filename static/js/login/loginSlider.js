let indiceActual = 0;

var tamañoSlide = 1000

function moverSlider(direccion) {
  const slides = document.getElementsByClassName('contenido-div');
  const totalDivs = slides.length;

  // Ajusta el índice actual basado en la dirección
  //console.log(indiceActual)
  //console.log('---')
  indiceActual = (indiceActual + direccion + totalDivs) % totalDivs;
  //console.log(indiceActual)
  const nuevoLeft = -indiceActual * tamañoSlide; // 500 debería ser el ancho de tus slides
  document.getElementById('slider').style.transform = `translateX(${nuevoLeft}px)`;
}


// Obtener una referencia al div
var miDiv = document.getElementById('contenedor-padre');

// Función para detectar el ancho del div y mostrarlo en la consola
function mostrarAnchoDiv() {
    var anchoDiv = miDiv.offsetWidth;

    let slider = document.getElementById('slider').style.width =  `${anchoDiv * 4}px`
    //console.log("Ancho del div:", anchoDiv, "px");
    //console.log("Slider: " + slider)
    tamañoSlide = anchoDiv 

    moverSlider(0)
}

// Llamar a la función para mostrar el ancho del div cuando se carga la página
mostrarAnchoDiv();

// Añadir un listener al evento resize de la ventana
window.addEventListener('resize', function() {
    // Llamar a la función para mostrar el ancho del div cada vez que se redimensiona la ventana
    mostrarAnchoDiv();
});
