$(document).ready(function () {
    $("#search-field-input").on("keyup", function () {
        var value = $(this).val().toLowerCase();
        $("#search-item .card").filter(function () {
            $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1);
            $(this).parent().toggle($(this).text().toLowerCase().indexOf(value) > -1);
        });
    });
});
