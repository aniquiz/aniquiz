var containersElts = document.getElementsByClassName("container");
var list_color_border = []

for (var i = 0; i < containersElts.length; i++) {
    list_color_border.push(getComputedStyle(containersElts[i]).borderBottomColor);
}

function set_true_radio_button(e) {
    /*
    Get the element listened by the 
    event listener, and then move to
    the input node to set his 
    value to true.
    Plus, change the border color of the
    container selected into green.
    */
    

    var target = e.currentTarget;
    var input_node = target.childNodes[1].childNodes[3];
    input_node.checked = true;

    for (var i = 0; i < containersElts.length; i++) {
        containersElts[i].style.borderColor = list_color_border[i];
    }
    target_style = getComputedStyle(target);
    target.style.borderColor = "#00cc00";
}

for (var i = 0; i < containersElts.length; i++) {
    containersElts[i].addEventListener("click", set_true_radio_button);
}
