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
    columDefs:[
    { className: "centered", targets: [0, 1, 2, 3, 4, 5, 6, 7, 8] },
    { orderable: false, targets: [7, 8] },
    {searchable: false, targets: [0, 2, 3, 4, 8] }
    ],
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

const initDataTable = async()=>{
    if(dataTableIsInitialized){
        dataTable.destroy();
    }

    await listAtomizado();

    dataTable=$('#datatable-atomizado').DataTable(dataTableOptions);

    dataTableIsInitialized = true;
};

const listAtomizado = async () =>{
    try{
        const response = await fetch("http://127.0.0.1:8000/webapp/list_atomizado/");
        const data = await response.json();
       let content=``;
        data.atomizado.forEach((atomizado, index)=>{
            content+=`
                <tr>
                    <td>${index+1}</td>
                    <td>${atomizado.fecha}</td>
                    <td>${atomizado.hora}</td>
                    <td>${atomizado.codigo}</td>
                    <td>${atomizado.planta}</td>
                    <td>${atomizado.nroSilo}</td>
                    <td>${atomizado.humedad}</td>
                    <td>${atomizado.usuario}</td>
                    <td>${atomizado.observaciones}</td>
                    <td>
                    <button class='btn btn-sm btn-primary'><i class='fa-solid fa-pencil' ></i></button>
                    <button class='btn btn-sm btn-danger'><i class='fa-solid fa-trash-can'></i></button>
                    <button class='btn btn-sm btn-secondary'></a><i class='fa-solid fa-eye'></i></button>
                    </td>
                </tr>
            `;

        });
        tableBody_atomizado.innerHTML = content;
    } catch(ex){
        alert(ex);
    }
};
window.addEventListener("load", async () => {
    await initDataTable();
});
