/*$(document).ready(function () {
            $('#example').DataTable();
        });
        */

$.extend(true, $.fn.dataTable.defaults, {
  //"searching": false,
  ordering: false,
});

$(document).ready(function () {
  var table = $("#example").DataTable({
    orderCellsTop: true,
    fixedHeader: true,
  });

  //Creamos una fila en el head de la tabla y lo clonamos para cada columna
  $("#example thead tr").clone(true).appendTo("#example thead");

  $("#example thead tr:eq(1) th").each(function (i) {
    var title = $(this).text(); //es el nombre de la columna
    $(this).html(
      '<input type="text" class="form-control" placeholder="Buscar.../>'
    );

    $("input", this).on("keyup change", function () {
      if (table.column(i).search() !== this.value) {
        table.column(i).search(this.value).draw();
      }
    });
  });

  $(".btn-exit-system").on("click", function (e) {
    e.preventDefault();
    Swal.fire({
      title: "¿Está seguro de cerrar sesión?",
      text: "Está a punto de cerrar la sesión y salir del sistema.",
      icon: "warning",
      type: "question",
      showCancelButton: true,
      confirmButtonColor: "#3085d6",
      cancelButtonColor: "#d33",
      confirmButtonText: "Sí, salir!",
      cancelButtonText: "No, cancelar",
    }).then((result) => {
      if (result.value) {
        window.location.href = "{% url 'planificacion:simulacion' %}";
      }
    });
  });

  //Animacion
  $(".animacion").on("click", function (e) {
    e.preventDefault();
    Swal.fire({
      title: "Custom width, padding, background.",
      width: 600,
      padding: "3em",
      background: "#fff url(/images/trees.png)",
      backdrop: `
                    rgba(0,0,123,0.4)
                    url("/nyan-cat-animated.gif")
                    left top
                    no-repeat
                `,
    });
  });
});
