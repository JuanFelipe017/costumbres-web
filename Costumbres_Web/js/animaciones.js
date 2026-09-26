// Animaciones compartidas: aparición al hacer scroll y estado del nav al bajar.
// Se carga en <head> para marcar <html class="anim"> antes del primer pintado; así el CSS
// oculta lo que va a aparecer sin parpadeo. Sin JS o con reduced-motion, nada se oculta.
(() => {
    const reducir = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    const animar = !reducir && 'IntersectionObserver' in window;
    const raiz = document.documentElement;
    if (animar) raiz.classList.add('anim');

    const PASO_MS = 80;      // separación entre tarjetas de un mismo grid
    const MAX_PASOS = 3;     // como máximo 4 escalones (0, 80, 160, 240 ms)
    const DURACION_MS = 600; // igual que --dur-reveal

    document.addEventListener('DOMContentLoaded', () => {
        // Nav: sombra y fondo al hacer scroll
        const nav = document.querySelector('nav.site-nav');
        if (nav) {
            const actualizar = () => nav.classList.toggle('is-scrolled', window.scrollY > 20);
            actualizar();
            window.addEventListener('scroll', actualizar, { passive: true });
        }

        if (!animar) return;
        try {
            const observer = new IntersectionObserver((entries) => {
                const visibles = entries
                    .filter(e => e.isIntersecting)
                    .map(e => e.target)
                    .sort((a, b) => (a.compareDocumentPosition(b) & Node.DOCUMENT_POSITION_FOLLOWING ? -1 : 1));
                const pasosPorGrupo = new Map();

                visibles.forEach(el => {
                    observer.unobserve(el);
                    const grupo = el.parentElement.matches('[data-anim="stagger"]') ? el.parentElement : el;
                    const paso = pasosPorGrupo.get(grupo) || 0;
                    pasosPorGrupo.set(grupo, paso + 1);
                    const retraso = Math.min(paso, MAX_PASOS) * PASO_MS;

                    el.style.setProperty('--reveal-delay', retraso + 'ms');
                    el.classList.add('is-visible');
                    // Al terminar, el elemento vuelve a sus estilos normales (hover, etc.)
                    setTimeout(() => {
                        el.classList.add('anim-done');
                        el.classList.remove('is-visible');
                        el.style.removeProperty('--reveal-delay');
                    }, DURACION_MS + retraso + 50);
                });
            }, { threshold: 0.12, rootMargin: '0px 0px -8% 0px' });

            document.querySelectorAll('[data-reveal], [data-anim="stagger"] > *').forEach(el => observer.observe(el));
        } catch (e) {
            raiz.classList.remove('anim'); // si algo falla, que todo quede visible
        }
    });
})();
