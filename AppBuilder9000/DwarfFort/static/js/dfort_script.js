

// Delete Modal
// Gets modal, button, and close button from dfort_edit.html
var modal = document.getElementById("delete-modal");
var btn = document.getElementById("button-modal");
var span = document.getElementsByClassName("close")[0];

// listener for click on button to open the modal
btn.onclick = function() {
    modal.style.display = "hidden";
}

// listener for click on close button
span.onclick = function() {
    modal.style.display = "none";
}

// listener for click outside of modal to close
window.onclick = function(event) {
    if(event.target == modal) {
        modal.style.display= "none";
    }
}