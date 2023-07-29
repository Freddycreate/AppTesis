let dataTable;
let dataTableIsInitialized = false;
let dataTableOptions = {
  dom: 'Bfrtilp',
  buttons: [
    {
      extend: 'excelHtml5',
      text: '<i class="fas fa-file-excel"></i> ',
      titleAttr: 'Exportar a Excel',
      className: 'btn btn-success',
    },
    {
      extend: 'pdfHtml5',
      text: '<i class="fas fa-file-pdf"></i> ',
      titleAttr: 'Exportar a PDF',
      className: 'btn btn-danger',
    },
    {
      extend: 'print',
      text: '<i class="fa fa-print"></i> ',
      titleAttr: 'Imprimir',
      className: 'btn btn-info',
    },
  ],
    columDefs: [
    { className: "centered", targets: [] },
    { orderable: false, targets: [] },
    {searchable: false, targets: [] },
    ],
    destroy: true,
    language: {
        lengthMenu: "Mostrar _MENU_ registros por página",
        zeroRecords: "Ningún usuario encontrado",
        info: "Mostrando del _START_ al _END_ de un total de _TOTAL_ registros",
        infoEmpty: "Ningún usuario encontrado",
        infoFiltered: "(filtrados desde _MAX_ registros totales)",
        search: "Buscar",
        loadingRecords: "Cargando ..",
        paginate: {
            firts: "Primero",
            last: "último",
            next: "Siguiente",
            previous: "Anterior"
        }
    }
};
const initDataTable=async()=>{
    if(dataTableIsInitialized){
        dataTable.destroy();
    }

    await listBarbotina();

    dataTable=$('#datatable-barbotina').DataTable(dataTableOptions);

    dataTableIsInitialized = true;
};

const listBarbotina = async () =>{
    try{
        const response = await fetch("http://127.0.0.1:8000/webapp/list_barbotina/");
        const data = await response.json();
       let content=``;
        data.barbotina.forEach((barbotina, id)=>{
            content+=`
                <tr>
                    <td>${barbotina.id}</td>
                    <td>${barbotina.fecha}</td>
                    <td>${barbotina.hora}</td>
                    <td>${barbotina.densidad}</td>
                    <td>${barbotina.viscosidad}</td>
                    <td>${barbotina.residuo}</td>
                    <td>${barbotina.planta}</td>
                    <td>${barbotina.usuario}</td>
                <td>
                    <button class='btn btn-sm btn-primary'><i class='fa-solid fa-pencil'></i></button>
                    <button class='btn btn-sm btn-danger'><i class='fa-solid fa-trash-can'></i></button>
                    <button class='btn btn-sm btn-secondary'><i class='fa-solid fa-eye'></i></button>
                    </td>


                </tr>
            `;
        });
        tableBody_barbotina.innerHTML = content;
    } catch(ex){
        alert(ex);
    }
};
window.addEventListener("load", async () => {
    await initDataTable();
});