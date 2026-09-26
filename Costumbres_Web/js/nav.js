// Menu movil (hamburguesa) - compartido por las 4 paginas
document.addEventListener('DOMContentLoaded', () => {
    const menuToggle = document.getElementById('menu-toggle');
    const mobileMenu = document.getElementById('mobile-menu');
    if (menuToggle && mobileMenu) {
        menuToggle.addEventListener('click', () => {
            const isOpen = mobileMenu.classList.contains('flex');
            mobileMenu.classList.toggle('hidden', isOpen);
            mobileMenu.classList.toggle('flex', !isOpen);
            menuToggle.querySelector('.material-symbols-outlined').textContent = isOpen ? 'menu' : 'close';
        });
    }

    // Sombra sutil en el nav al hacer scroll (no le cambia el alto, para que no se vea "pegado")
    const siteNav = document.querySelector('nav.site-nav');
    if (siteNav) {
        window.addEventListener('scroll', () => {
            siteNav.classList.toggle('shadow-md', window.scrollY > 20);
        });
    }
});
