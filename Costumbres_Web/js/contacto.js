// Modal de garantía con <dialog> nativo: cierra con Esc, atrapa el foco y lo devuelve al botón al cerrar.
document.addEventListener('DOMContentLoaded', () => {
    const dialogo = document.getElementById('modal-garantia');
    if (!dialogo) return;

    const abrir = () => {
        if (typeof dialogo.showModal === 'function') dialogo.showModal();
        else dialogo.setAttribute('open', '');
    };
    const cerrar = () => {
        if (typeof dialogo.close === 'function') dialogo.close();
        else dialogo.removeAttribute('open');
    };

    document.querySelectorAll('[data-open-garantia]').forEach(b => b.addEventListener('click', abrir));
    dialogo.querySelectorAll('[data-close-dialog]').forEach(b => b.addEventListener('click', cerrar));
    // Clic en el fondo oscuro (fuera de la tarjeta) también cierra
    dialogo.addEventListener('click', (e) => {
        if (e.target === dialogo) cerrar();
    });
});
