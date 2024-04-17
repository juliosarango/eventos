function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function armarRequestAjax(path, csrftoken, form) {

    // csrftoken puede estar vacio si las variables CSRF_USE_SESSIONS CSRF_COOKIE_HTTPONLY están en false
    if (csrftoken == '') {
        const csrftoken = getCookie('csrftoken');
    }

    const request = new Request(
        path,
        {
            method: 'POST',
            headers: { 'X-CSRFToken': csrftoken },
            mode: 'same-origin',
            body: form
        }
    )
    return request
}


function retornarCampos(tipo = 0, datos) {

    let razon_social = ''
    if (tipo == 0) {
        razon_social = datos.datos.razon_social
    } else {
        razon_social = datos.datos[1].Valor
    }

    let camposEmail = '<div class="input-group mb-3">'
    camposEmail += '<span style="width:160px;" class="input-group-text">Email</span>'
    camposEmail += '<input type="text" class="form-control" placeholder="info@entidad.com" aria-label="Email" id="email" name="email">'
    camposEmail += '</div>'

    let campos = ''

    if (tipo == 0) {
        campos += '<div id="camposRegistro">'
        campos += '<div class="input-group mb-3">'
        campos += '<span style="width:160px;" class="input-group-text">Entidad</span>'
        campos += '<input type="text" class="form-control" aria-label="Entidad" disabled=disabled value="' + razon_social + '">'
        campos += '<input type="hidden" class="form-control" id="entidad" name="entidad" value="' + razon_social + '">'
        campos += '</div>'
        campos += camposEmail
        campos += '<div class="input-group mb-3">'
        campos += '<span style="width:160px;" class="input-group-text">Usuario SOCE</span>'
        campos += '<input type="text" class="form-control" placeholder="username" aria-label="Usuario" id="usuario" name="usuario">'
        campos += '</div>'
        campos += '<div class="input-group mb-3">'
        campos += '<span style="width:160px;" class="input-group-text">Password SOCE</span>'
        campos += '<input type="password" class="form-control" placeholder="password" aria-label="passwordsoce" id="passwordsoce" name="passwordsoce">'
        campos += '</div>'
        campos += '</div>'
    } else if (tipo == 1) {
        campos += '<div id="camposRegistro">'
        campos += '<div class="input-group mb-3">'
        campos += '<span style="width:160px;" class="input-group-text">Nombres</span>'
        campos += '<input type="text" class="form-control" aria-label="Ciudadano" disabled=disabled value="' + razon_social + '">'
        campos += '<input type="hidden" class="form-control" id="ciudadano" name="ciudadano" value="' + razon_social + '">'
        campos += '</div>'
        campos += camposEmail
        campos += '</div>'
    }
    campos += '<div id="spinner-grabar"></div>'

    return campos
}

function retornarBoton(op) {
    return `<button type="button" class="btn btn-primary" onClick="registrarDatos(${op})">Guardar</button>`
}
