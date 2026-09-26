// Menu movil (hamburguesa) - compartido por todas las paginas
document.addEventListener('DOMContentLoaded', () => {
    const menuToggle = document.getElementById('menu-toggle');
    const mobileMenu = document.getElementById('mobile-menu');
    if (menuToggle && mobileMenu) {
        const icono = menuToggle.querySelector('.material-symbols-outlined');
        const setOpen = (open) => {
            mobileMenu.classList.toggle('hidden', !open);
            mobileMenu.classList.toggle('flex', open);
            menuToggle.setAttribute('aria-expanded', String(open));
            menuToggle.setAttribute('aria-label', open ? menuToggle.dataset.labelClose : menuToggle.dataset.labelOpen);
            icono.textContent = open ? 'close' : 'menu';
        };
        menuToggle.addEventListener('click', () => setOpen(menuToggle.getAttribute('aria-expanded') !== 'true'));
        // Esc cierra el menu y devuelve el foco al boton
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape' && menuToggle.getAttribute('aria-expanded') === 'true') {
                setOpen(false);
                menuToggle.focus();
            }
        });
    }

    // Sombra sutil en el nav al hacer scroll (no le cambia el alto, para que no se vea "pegado")
    const siteNav = document.querySelector('nav.site-nav');
    if (siteNav) {
        window.addEventListener('scroll', () => {
            siteNav.classList.toggle('shadow-md', window.scrollY > 20);
        }, { passive: true });
    }
});
