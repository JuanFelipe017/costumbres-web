 // Aparición suave de los bloques [data-reveal] al hacer scroll (historia y categorías).
// Si el usuario pidió reducir movimiento o el navegador no soporta IntersectionObserver,
// no se oculta nada: el contenido siempre queda visible aunque este script falle.
(() => {
    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
    if (!('IntersectionObserver' in window)) return;

    const OCULTO = ['opacity-0', 'translate-y-10'];
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (!entry.isIntersecting) return;
            entry.target.classList.remove(...OCULTO);
            observer.unobserve(entry.target);
            // Al terminar, quitar la duración larga para que los hover vuelvan a ser rápidos
            setTimeout(() => entry.target.classList.remove('duration-1000'), 1000);
        });
    }, { threshold: 0.1 });

    document.querySelectorAll('[data-reveal]').forEach(el => {
        if (el.getBoundingClientRect().top < window.innerHeight) return; // ya visible al cargar
        el.classList.add('transition-all', 'duration-1000', ...OCULTO);
        observer.observe(el);
    });
})();
