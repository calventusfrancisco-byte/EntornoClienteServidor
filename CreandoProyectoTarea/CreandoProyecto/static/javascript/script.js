const boton1 = document.getElementById("acogida");
const boton2 = document.getElementById("contacto");
const boton3 = document.getElementById("BotonPagPrincipal");

boton1?.addEventListener("click", () => {
    window.location.href = "/primeraApp/";
});

boton2?.addEventListener("click", () => {
    window.location.href = "/primeraApp/contacto";
});

boton3?.addEventListener("click", () => {
    window.location.href = "/";
});