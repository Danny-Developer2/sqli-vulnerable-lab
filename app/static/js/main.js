/* SQLi Vulnerable Lab - interacciones mínimas de demostración */

document.addEventListener("DOMContentLoaded", function () {
  // Botones "chip": rellenan el campo y envían el formulario con un payload.
  document.querySelectorAll(".chip").forEach(function (chip) {
    chip.addEventListener("click", function () {
      var field = document.querySelector('[name="' + chip.dataset.target + '"]');
      if (!field) return;
      field.value = chip.dataset.value;
      var form = field.closest("form");
      if (form) form.submit();
    });
  });

  // Confirmación antes de cerrar sesión.
  document.querySelectorAll("[data-confirm]").forEach(function (link) {
    link.addEventListener("click", function (event) {
      if (!window.confirm("¿Cerrar sesión?")) {
        event.preventDefault();
      }
    });
  });

  // Marca visual de la consulta SQL mostrada en la página de resultados.
  document.querySelectorAll(".sql-box pre code").forEach(function (block) {
    block.setAttribute("data-testid", "executed-sql");
  });
});
