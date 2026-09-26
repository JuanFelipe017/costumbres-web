// Visor de fotos (lightbox) con <dialog> nativo.
// - [data-carousel]: abre todas las fotos de esa técnica, empezando por la que se ve.
// - [data-visor="grupo"]: fotos sueltas; las que comparten grupo se recorren juntas.
// Teclado: flechas para navegar, Esc para cerrar. Celular: deslizar a los lados.
document.addEventListener('DOMContentLoaded', () => {
    const en = document.documentElement.lang === 'en';
    const TXT = en
        ? { ampliar: 'View larger', cerrar: 'Close', anterior: 'Previous photo', siguiente: 'Next photo', visor: 'Photo viewer', de: 'of' }
        : { ampliar: 'Ampliar foto', cerrar: 'Cerrar', anterior: 'Foto anterior', siguiente: 'Foto siguiente', visor: 'Visor de fotos', de: 'de' };
    const icono = (nombre) => `<span class="material-symbols-outlined" aria-hidden="true">${nombre}</span>`;

    const carruseles = document.querySelectorAll('[data-carousel]');
    const sueltas = document.querySelectorAll('[data-visor]');
    if (!carruseles.length && !sueltas.length) return;

    // ---- Diálogo (uno solo por página) ----
    const dialogo = document.createElement('dialog');
    dialogo.className = 'visor';
    dialogo.setAttribute('aria-label', TXT.visor);
    dialogo.innerHTML = `
        <figure class="visor-figura">
            <img class="visor-img" alt="" />
            <figcaption class="visor-pie"><span class="visor-texto"></span><span class="visor-contador"></span></figcaption>
        </figure>
        <button type="button" class="visor-btn visor-cerrar" aria-label="${TXT.cerrar}">${icono('close')}</button>
        <button type="button" class="visor-btn visor-anterior" aria-label="${TXT.anterior}">${icono('chevron_left')}</button>
        <button type="button" class="visor-btn visor-siguiente" aria-label="${TXT.siguiente}">${icono('chevron_right')}</button>`;
    document.body.appendChild(dialogo);

    const img = dialogo.querySelector('.visor-img');
    const texto = dialogo.querySelector('.visor-texto');
    const contador = dialogo.querySelector('.visor-contador');
    const btnAnterior = dialogo.querySelector('.visor-anterior');
    const btnSiguiente = dialogo.querySelector('.visor-siguiente');

    let fotos = []; // [{ src, alt }]
    let actual = 0;

    const mostrar = async (i) => {
        actual = (i + fotos.length) % fotos.length;
        const foto = fotos[actual];
        img.classList.add('is-cambiando');
        img.src = foto.src;
        img.alt = foto.alt;
        try { await img.decode(); } catch (e) { /* igual se muestra */ }
        img.classList.remove('is-cambiando');
        texto.textContent = foto.alt;
        contador.textContent = fotos.length > 1 ? `${actual + 1} ${TXT.de} ${fotos.length}` : '';
    };

    const abrir = (lista, inicio) => {
        fotos = lista;
        const varias = lista.length > 1;
        btnAnterior.hidden = !varias;
        btnSiguiente.hidden = !varias;
        mostrar(inicio);
        if (typeof dialogo.showModal === 'function') dialogo.showModal();
        else dialogo.setAttribute('open', '');
    };
    const cerrar = () => {
        if (typeof dialogo.close === 'function') dialogo.close();
        else dialogo.removeAttribute('open');
    };

    dialogo.querySelector('.visor-cerrar').addEventListener('click', cerrar);
    btnAnterior.addEventListener('click', () => mostrar(actual - 1));
    btnSiguiente.addEventListener('click', () => mostrar(actual + 1));
    dialogo.addEventListener('click', (e) => { if (e.target === dialogo) cerrar(); });
    dialogo.addEventListener('keydown', (e) => {
        if (fotos.length < 2) return;
        if (e.key === 'ArrowLeft') mostrar(actual - 1);
        if (e.key === 'ArrowRight') mostrar(actual + 1);
    });

    // Deslizar en el celular
    let inicioX = null;
    dialogo.addEventListener('pointerdown', (e) => { inicioX = e.clientX; });
    dialogo.addEventListener('pointerup', (e) => {
        if (inicioX === null || fotos.length < 2) return;
        const dx = e.clientX - inicioX;
        inicioX = null;
        if (Math.abs(dx) > 50) mostrar(actual + (dx < 0 ? 1 : -1));
    });

    // ---- Carruseles de técnicas: botón de lupa + clic en la foto ----
    carruseles.forEach(container => {
        let lista;
        try { lista = JSON.parse(container.getAttribute('data-carousel')); } catch (e) { return; }
        const alt = container.querySelector('img') ? container.querySelector('img').alt : '';
        const abrirCarrusel = () => abrir(lista.map(src => ({ src, alt })), parseInt(container.dataset.index || '0', 10));

        const boton = document.createElement('button');
        boton.type = 'button';
        boton.className = 'absolute bottom-3 left-3 z-10 w-11 h-11 rounded-full bg-surface/90 text-on-surface shadow-md flex items-center justify-center hover:bg-surface transition-colors';
        boton.setAttribute('aria-label', `${TXT.ampliar}: ${alt}`);
        boton.innerHTML = icono('zoom_in');
        boton.addEventListener('click', abrirCarrusel);
        container.appendChild(boton);

        container.classList.add('visor-disparador');
        container.addEventListener('click', (e) => {
            if (!e.target.closest('button')) abrirCarrusel();
        });
    });

    // ---- Fotos sueltas / en grupo ----
    const grupos = new Map();
    sueltas.forEach(el => {
        const clave = el.dataset.visor || el;
        if (!grupos.has(clave)) grupos.set(clave, []);
        grupos.get(clave).push(el);
    });
    grupos.forEach(elementos => {
        const lista = elementos.map(el => {
            const foto = el.querySelector('img');
            return { src: foto.currentSrc || foto.src, alt: foto.alt };
        });
        elementos.forEach((el, i) => {
            el.classList.add('visor-disparador');
            el.setAttribute('role', 'button');
            el.setAttribute('tabindex', '0');
            el.setAttribute('aria-label', `${TXT.ampliar}: ${lista[i].alt}`);
            el.addEventListener('click', () => abrir(lista, i));
            el.addEventListener('keydown', (e) => {
                if (e.key === 'Enter' || e.key === ' ') {
                    e.preventDefault();
                    abrir(lista, i);
                }
            });
        });
    });
});
