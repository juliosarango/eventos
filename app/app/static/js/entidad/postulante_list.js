const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

function buscarDatos() {
    mostrarSpinner('spinner-buscar');
    const formData = document.getElementById('frmDatos');
    const form = new FormData(formData);

    if (csrftoken == '') {
        const csrftoken = getCookie('csrftoken');
    }

    const request = new Request(
        '../verifica_ciudadano/',
        {
            method: 'POST',
            headers: { 'X-CSRFToken': csrftoken },
            mode: 'same-origin',
            body: form
        }
    )

    fetch(request)
        .then(response => {
            return response.json()
        })
        .then(data => {
            quitarSpinner('spinner-buscar')
            if (data.status == 'ok') {
                if (data.tipo == 'C')
                    location.href = "/postulante_ciudadano";
                else
                    location.href = "new/" + form.get("ruc").toString();
            }
            if (data.status == 'val') {
                lanzarAlert('Error', data.message, 'error')
            }
            if (data.status == 'vincular') {
                Swal.fire({
                    title: "Advertencia",
                    text: data.message,
                    icon: "question",
                    showCancelButton: true,
                    cancelButtonText: "Cancelar",
                    confirmButtonText: "Aceptar",
                    reverseButtons: true
                }).then((result) => {
                    if (result.isConfirmed) {
                        location.href = "vincular/" + data.id;
                    } else {
                        window.location.href = "/postulante";
                    }
                })
            }
            if (data.status == 'empty') {
                Swal.fire({
                    title: "Advertencia",
                    text: "El número de identificación ingresado no pudo ser verificado desea continuar.?",
                    icon: "question",
                    showCancelButton: true,
                    cancelButtonText: "Cancelar",
                    confirmButtonText: "Aceptar",
                    reverseButtons: true
                }).then((result) => {
                    if (result.isConfirmed) {
                        location.href = "new/" + form.get("ruc").toString();
                    } else {
                        window.location.href = "/postulante";
                    }
                })
            }
        })
        .catch(err => {
            quitarSpinner('spinner-buscar')
            lanzarAlert('Error', "Problemas al procesar el registro, intente nuevamente.", 'error')
        })
}


function mostrarSpinner(id_elemento, op = 0) {
    let spinner = ''
    if (op == 0) {
        spinner = `<span class="spinner-grow spinner-grow-sm" role="status" aria-hidden="true"></span>...`
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
    document.getElementById(id_elemento).innerHTML = spinner
}


function quitarSpinner(id_elemento) {
    document.getElementById(id_elemento).innerHTML = ''
}


function lanzarAlert(title, message, icon) {
    Swal.fire({
        title: title,
        text: message,
        icon: icon,
        confirmButtonText: 'Aceptar'
    })
        .then((res) => {
            if (res.isConfirmed) {
                reinicarCampos()
            }
        })
}


function reinicarCampos() {
    //document.getElementById('ruc').value = ''
    //location.reload();
}