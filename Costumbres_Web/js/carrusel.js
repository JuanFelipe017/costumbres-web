// Carrusel automático de fotos por tarjeta, con botón de pausa (WCAG 2.2.2).
// No arranca solo si el usuario pidió reducir movimiento, y solo avanza mientras la tarjeta está en pantalla.
document.addEventListener('DOMContentLoaded', () => {
    const INTERVALO_MS = 3500; // cada cuánto cambia de foto
    const reducirMovimiento = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    const en = document.documentElement.lang === 'en';
    const TXT = en
        ? { pausar: 'Pause photos', reproducir: 'Play photos' }
        : { pausar: 'Pausar fotos', reproducir: 'Reproducir fotos' };

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
        let pausado = reducirMovimiento;
        let visible = false;

        const boton = document.createElement('button');
        boton.type = 'button';
        boton.className = 'absolute bottom-3 right-3 z-10 w-11 h-11 rounded-full bg-surface/90 text-on-surface shadow-md flex items-center justify-center hover:bg-surface transition-colors';
        boton.innerHTML = '<span class="material-symbols-outlined" aria-hidden="true"></span>';
        const pintarBoton = () => {
            boton.setAttribute('aria-label', pausado ? TXT.reproducir : TXT.pausar);
            boton.firstChild.textContent = pausado ? 'play_arrow' : 'pause';
        };
        boton.addEventListener('click', () => {
            pausado = !pausado;
            pintarBoton();
        });
        pintarBoton();
        container.appendChild(boton);

        if ('IntersectionObserver' in window) {
            new IntersectionObserver(entries => {
                visible = entries[0].isIntersecting;
            }).observe(container);
        } else {
            visible = true;
        }

        let cambiando = false;
        setInterval(async () => {
            if (pausado || !visible || document.hidden || cambiando) return;
            cambiando = true;
            indiceActual = (indiceActual + 1) % imagenes.length;
            const capaEntrante = capas[capaActiva === 0 ? 1 : 0];
            const capaSaliente = capas[capaActiva];

            // Esperar a que la foto nueva esté descargada antes del fundido (evita el cuadro en blanco)
            capaEntrante.loading = 'eager';
            capaEntrante.src = imagenes[indiceActual];
            try { await capaEntrante.decode(); } catch (e) { /* si falla, igual se muestra */ }
            cambiando = false;
            capaEntrante.classList.remove('opacity-0');
            capaEntrante.classList.add('opacity-100');
            capaEntrante.removeAttribute('aria-hidden');
            capaSaliente.classList.remove('opacity-100');
            capaSaliente.classList.add('opacity-0');
            capaSaliente.setAttribute('aria-hidden', 'true');

            capaActiva = capaActiva === 0 ? 1 : 0;
        }, INTERVALO_MS);
    });
});
