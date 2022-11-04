$(document).ready(function () {
    $("#search-field-input").on("keyup", function () {
        var value = $(this).val().toLowerCase();
        $("#search-item .search-card").filter(function () {
            $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1);
            $(this).parent().toggle($(this).text().toLowerCase().indexOf(value) > -1);
        });
        var allCards = $("#search-item > .search-card");
        var allHiddenCards = allCards.filter(function(){ return ($(this).css("display") == "none"); })
        if (allCards.length == allHiddenCards.length) {
            $("#offers #carousel").css("height", "475");
        }
        else {
            $("#offers #carousel").css("height", "auto");
        }
    });
});
