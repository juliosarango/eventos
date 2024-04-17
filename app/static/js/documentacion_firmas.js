function generate_btn_descarga(link){
    const btn = document.createElement("a");
    btn.setAttribute("href", link);
    btn.setAttribute("target", "_blank");

    const img = document.createElement("i");
    img.setAttribute("class", "bi bi-cloud-download");

    const text = document.createTextNode(" Descargar Archivo");

    btn.appendChild(img);
    btn.appendChild(text);

    return btn;
}

function generate_btn_verify_signatures(id){
    const btn = document.createElement("a");
    btn.setAttribute("class", "btn btn-outline-primary");
    btn.setAttribute("data-bs-target", "#modalFirmas");
    btn.setAttribute("data-bs-toggle", "modal");
    btn.setAttribute("data-bs-dismiss", "modal");
    btn.setAttribute("onclick", "get_signatures('" + id + "')");

    const img = document.createElement("i");
    img.setAttribute("class", "bi bi-pen-fill");
    const cellText = document.createTextNode(" Ver Firmas");

    btn.appendChild(img);
    btn.appendChild(cellText);

    return btn;
}

function generate_cell(innerHTML, tag="td"){
    const cell = document.createElement(tag);
    const cellText = document.createTextNode(innerHTML);
    cell.appendChild(cellText);

    return cell;
}

function generate_header(){
    // generating table header
    const tblHead = document.createElement("thead");
    tblHead.setAttribute("class", "table-dark text-center");
    tblHead.setAttribute("style", "margin: auto;");
    const row = document.createElement("tr");

    const lst_table_header = [
        "#",
        "Descargar",
        "Nombre Original",
        "Fecha Registro",
        "Firmas",
    ]
    lst_table_header.forEach(innerHTML => {
        row.appendChild(generate_cell(innerHTML, tag="th"));
        tblHead.appendChild(row);
    });

    return tblHead;
}

function generate_table(data){
    const tbl = document.createElement("table");
    tbl.setAttribute("class", "table table-bordered table-striped table-sm");

    const tblBody = document.createElement("tbody");

    // creating all cells
    let row_number = 0;
    data.forEach(row_data => {
        row_number = row_number + 1;
        const row = document.createElement("tr");
        row.appendChild(generate_cell(row_number));
        for (const [key, value] of Object.entries(row_data)) {
            if (key === "firma_id"){
                const tr = document.createElement("tr");
                tr.appendChild(generate_btn_verify_signatures(value));
                row.appendChild(tr);
            }
            else if (key === "descarga"){
                const tr = document.createElement("tr");
                tr.appendChild(generate_btn_descarga(value));
                row.appendChild(tr);
            }
            else{
                row.appendChild(generate_cell(value));
            }
        }
        tblBody.appendChild(row);
    });

    // put the <thead> in the <table>
    tbl.appendChild(generate_header());
    // put the <tbody> in the <table>
    tbl.appendChild(tblBody);

    return tbl;
}

async function get_documents(postulacion_id){
    mostrarSpinner("documents", op = 2);
    let url = "/documents/" + postulacion_id;
    await fetch(url, {
        headers: {'Content-Type': 'application/json'},
    }).then(response => {
        return response.json();
    }).then(data => {
        if (!data){
            const no_data_h5 = document.createElement("h5");
            no_data_h5.innerHTML = "No existen firmas válidas";
            documents.innerHTML = "";
            documents.appendChild(no_data_h5);
        }
        else{
            documents.innerHTML = "";
            documents.appendChild(generate_table(data));
        }
    });
}

async function get_signatures(archivo_id){
    mostrarSpinner("contenido", op = 2);
    let url = "/documentacion/detalle_firmas/" + archivo_id;
    await fetch(url, {
        headers: {'Content-Type': 'application/json'},
    }).then(response => {
        return response.text();
    }).then(body => {
        contenido.innerHTML = "";
        contenido.innerHTML = body;
    });
}
