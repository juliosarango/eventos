function lanzarMensaje(title, message, icon, after_confirm_function = undefined) {
    Swal.fire({
        title: title,
        text: message,
        icon: icon,
        confirmButtonText: 'Aceptar'
    })
        .then((res) => {
            if (res.isConfirmed && after_confirm_function != undefined) {
                after_confirm_function;
            }
        });
}
function mostrarSpinner(id_elemento, op = 0) {
    let spinner = ''
    if (op == 0) {
        spinner = `
                <span class="spinner-grow spinner-grow-sm" role="status" aria-hidden="true"></span>
                ...`
    } else {
        spinner = `
            <div class="text-center">
              <div class="spinner-border" style="width: 3rem; height: 3rem;" role="status">
                <span class="visually-hidden">Loading...</span>
              </div>
              <div class="spinner-grow" style="width: 3rem; height: 3rem;" role="status">
                <span class="visually-hidden">Loading...</span>
              </div>
            </div>`

    }
    document.getElementById(id_elemento).innerHTML = spinner;
}
function quitarSpinner(id_elemento) {
    document.getElementById(id_elemento).innerHTML = '';
}