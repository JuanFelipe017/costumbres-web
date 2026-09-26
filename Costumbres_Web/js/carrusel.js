// Carrusel automático de fotos por tarjeta 
document.addEventListener('DOMContentLoaded', () => {
    const INTERVALO_MS = 3500; // cada cuánto cambia de foto

    document.querySelectorAll('[data-carousel]').forEach(container => {
        let imagenes;
        try {
            imagenes = JSON.parse(container.getAttribute('data-carousel'));
        } catch (e) {
            return;
        }
        if (!imagenes || imagenes.length < 2) return; // 1 sola foto: no hay nada que rotar

        const capas = container.querySelectorAll('.carousel-img');
        if (capas.length < 2) return;

        let indiceActual = 0;
        let capaActiva = 0;

        setInterval(() => {
            indiceActual = (indiceActual + 1) % imagenes.length;
            const capaEntrante = capas[capaActiva === 0 ? 1 : 0];
            const capaSaliente = capas[capaActiva];

            capaEntrante.src = imagenes[indiceActual];
            capaEntrante.classList.remove('opacity-0');
            capaEntrante.classList.add('opacity-100');
            capaSaliente.classList.remove('opacity-100');
            capaSaliente.classList.add('opacity-0');

            capaActiva = capaActiva === 0 ? 1 : 0;
        }, INTERVALO_MS);
    });
});