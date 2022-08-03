
$(document).ready(function() {
    console.log('ready!');

    // AJAX method to get discogs/pitchfork data as json
    // without page refresh
    $('#catalog-widget').submit(function(event) {
        event.preventDefault();
        $.ajax({
            url: this.action,
            type: this.method,
            data: {cat_number: $('#cat_number').val()},
            dataType: 'json',
        }).done(function(json) {
            console.log(json);
            populateForm(json);
            displayAlbum(json);
        })
    });
});

function populateForm(json) {
   document.getElementById('id_title').value = json['title']
   document.getElementById('id_format').value = json['format']
   document.getElementById('id_genre').value = json['genre']
   document.getElementById('id_country').value = json['country']
   document.getElementById('id_style').value = json['style']
   document.getElementById('id_label').value = json['label'][0]
   document.getElementById('id_pf_rating').value = json['pitchfork_score']
   document.getElementById('id_cover_image').value = json['cover_image']
}

function displayAlbum(json) {
    document.getElementById('release-form-image').src = json['cover_image'];
    document.getElementById('release-form-wrap').style.display = 'block';
}