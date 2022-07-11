

// Delete Modal
// Gets modal, button, and close button from dfort_edit.html
var modal = document.getElementById("delete-modal");
var btn = document.getElementById("button-modal");
var close = document.getElementById("modal-close");

// listener for click on button to open the modal
btn.onclick = function() {
    modal.style.display = "block";
}

// listener for click on close button
close.onclick = function() {
    modal.style.display = "none";
}