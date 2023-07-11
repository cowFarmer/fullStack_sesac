const input_field = document.getElementById("input_field");
const input_buttons = document.querySelectorAll("button");

const valid_input = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "*", "+", "-", "/", "=", "Backspace"];
const enter = ["Enter", "="];
const cancle = ["Escape", "C"];

function cal_result(data) {
    /*
    계산
    */
    return eval(data);
}

input_field.addEventListener("keydown", function(e) {
    /*
    input_field keydown event handler
    */
    const keyPressed = e.key;

    if (valid_input.includes(keyPressed)) {
        // pass
    } else if (enter.includes(keyPressed)) {
        input_field.value = cal_result(input_field.value);
    } else if (cancle.includes(keyPressed)) {
        input_field.value = ""
    } else {
        e.preventDefault();
    }
});

input_buttons.forEach(function(button) {
    /*
    button click event handler
    */
    button.addEventListener("click", function (e) {
        if (enter.includes(button.textContent)) {
            input_field.value = cal_result(input_field.value);
        } else if (cancle.includes(button.textContent)) {
            input_field.value = "";
        } else {
            input_field.value += button.textContent;
        } 
    });
});