$(window).on('load', function() {
	$("body").removeClass('fade-out')
});

$("#delete-game-button").on('click', function(){
    return confirm('Are you sure you want to delete this game?')
})

$("#pull-from-bgg").on('click', function() {
    // I really wanted to use python for this, and the code was _relatively_ easier, but I decided it was
    // very important in terms of flow to have this functionality client-side.
    // gameid is the unique value used by Board Game Geek to identify a board game.
    var gameid = prompt("Enter the gameid for the game you would like to pull.\nThis is an integer between one and six digits.\nOnce you find the game on https://www.boardgamegeek.com,\nthe page for the game is in the following format:\nhttps://boardgamegeek.com/boardgame/<gameid>/<name>", "")

    //Ensuring the given value for gameid is a positive integer with equal to or less than six digits.
    if (parseInt(gameid) && parseInt(gameid) > 0 && gameid.length <= 6) {
        // Instructions for the API are here: https://boardgamegeek.com/wiki/page/BGG_XML_API2
        var url = "https://api.geekdo.com/xmlapi2/thing?thing=boardgame&id=" + gameid
        // $.ajax is a jQuery function used for pulling JSON or XML data from an API.
        $.ajax({
            url: url,
            dataType: 'xml',
            success: function(xml) {
                // Determining these values was a several hours long process of trial and error and frustration.
                // And searching Google (and primarily Stack Overflow) for help was mostly fruitless.
                $("#id_Description").val($(xml).find('description').eq(0).text())
                $("#id_Image").val($(xml).find('image').eq(0).text())
                $("#id_Thumbnail").val($(xml).find('thumbnail').eq(0).text())

                // When I finally determined what to do for image, thumbnail, and description, I tried .attr().  No luck.
                // Searching through the object I found the attributes node had the data I needed.
                // By sheer luck, adding .value got the data I needed.
                $("#id_Name").val($(xml).find('name').eq(0)[0].attributes['value'].value)
                $("#id_Year").val($(xml).find('yearpublished').eq(0)[0].attributes['value'].value)

                // There was a Stack Overflow entry for working with Python that helped me with searching by attribute.
                //     It was really helpful for finding the publisher.  In JavaScript I needed to remove the @ sign.
                $("#id_Publisher").val($(xml).find('link[type="boardgamepublisher"]').eq(0)[0].attributes['value'].value)
            }
        })
    }
})