document.addEventListener('DOMContentLoaded', (event) => {
    console.log('DOM completamente cargado y analizado');
    const btnEliminacion = document.querySelectorAll('.btneliminacion');

    btnEliminacion.forEach(btn => {
        btn.addEventListener('click', (e) => {
            const confirmacion = confirm("¿Seguro de eliminar el curso?");
            if (!confirmacion) {
                e.preventDefault();
            }
        });
    });
});
