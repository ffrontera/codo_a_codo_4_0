const botonReceta = document.getElementById("receta-btn");
const receta = document.getElementById("receta");
const xReceta = document.getElementById('xReceta');
const secciones = document.getElementsByTagName('section');

function mostrarSeccion(indicador){
    for(i = 0; i < secciones.length; i++) {
        if(secciones[i].id == indicador)
            secciones[i].style.display = "block";
        else
            secciones[i].style.display = "none";
    }
}

function mostrarReceta() {
    document.getElementById('home').style.display = "flex";
    receta.style.display = "block";
    botonReceta.style.display = "none";
}

function ocultarReceta() {
    mostrarSeccion('home');
    receta.style.display = "none";
    botonReceta.style.display = "block";
}