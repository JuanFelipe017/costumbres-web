document.querySelectorAll('input, textarea, select').forEach(el => {
    el.addEventListener('focus', () => {
        el.parentElement.querySelector('label').classList.add('text-primary');
    });
    el.addEventListener('blur', () => {
        el.parentElement.querySelector('label').classList.remove('text-primary');
    });
});

function abrirGarantia() {
    const modal = document.getElementById("modalGarantia");

    modal.classList.remove("hidden");
    modal.classList.add("flex");
}

function cerrarGarantia() {
    const modal = document.getElementById("modalGarantia");

    modal.classList.remove("flex");
    modal.classList.add("hidden");
}