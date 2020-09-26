var containersElts = document.getElementsByClassName("container");

function set_true_radio_button(e) {
    // Get the element listened by the 
    // event listener, and then move to
    // the input node to change his value.
    
    var target = e.currentTarget;
    var input_node = target.childNodes[1].childNodes[3];
    input_node.checked = true;
}

for (var i = 0; i < containersElts.length; i++) {
    containersElts[i].addEventListener("click", set_true_radio_button);
}
