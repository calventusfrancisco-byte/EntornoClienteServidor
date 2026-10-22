const boton1 = document.getElementById("acogida");
const boton2 = document.getElementById("contacto");
const boton3 = document.getElementById("BotonPagPrincipal");
const boton4 = document.getElementById("BotonCalendario");

if(nombreHTML == 'calendario.html')
{
let textoComprobacion = document.getElementById("comprobacion");
if(dia == 22)
{
    textoComprobacion.textContent = "Hoy es 22";
}
}

boton1?.addEventListener("click", () => {
    window.location.href = "/primeraApp/";
});

boton2?.addEventListener("click", () => {
    window.location.href = "/primeraApp/contacto";
});

boton3?.addEventListener("click", () => {
    window.location.href = "/";
});

boton4?.addEventListener("click", () => {
    window.location.href = "/primeraApp/calendario";
});

