$('catalog-widget').on('submit', function(e) {
    e.preventDefault();
    $.ajax({
        url: 'VinylCollection/test/',
        type: this.method,
        dataType: 'json',
        success: function(response) {
            $('#testing').html(response);
        }
    }).done(function(json) {
        $("<h1>").text(json.title).appendTo("body");
    }).fail(function(xhr, status, errorThrown) {
        alert("Sorry, there was a problem.");
        console.log("Error: " + errorThrown);
        console.log("Status: " + status);
        console.dir(xhr);
    }).always(function(xhr, status) {
        alert("The request is complete.");
    })
});