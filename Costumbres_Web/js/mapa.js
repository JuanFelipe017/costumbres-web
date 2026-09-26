// Mapa de Google bajo demanda: el iframe (y sus cookies) solo se carga cuando el usuario pulsa "Cargar mapa".
document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.map-facade').forEach(facade => {
        const boton = facade.querySelector('.map-load');
        if (!boton) return;
        boton.addEventListener('click', () => {
            const iframe = document.createElement('iframe');
            iframe.src = facade.dataset.mapSrc;
            iframe.title = facade.dataset.mapTitle;
            iframe.className = 'w-full h-full border-0';
            iframe.setAttribute('allowfullscreen', '');
            iframe.setAttribute('referrerpolicy', 'no-referrer-when-downgrade');
            facade.replaceWith(iframe);
            iframe.focus();
        });
    });
});
