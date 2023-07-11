const input_field = document.getElementById("input_field");
const input_buttons = document.querySelectorAll("button");

function cal_result(data) {
    return eval(data);
}

input_field.addEventListener("keydown", function(e) {
    const valid_input = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "*", "+", "-", "/", "=", "Backspace"];
    const enter = ["Enter"];
    const cancle = ["Escape", "C"];
    const keyPressed = e.key;

    if (enter.includes(keyPressed)) {
        input_field.value = cal_result(input_field.value);
    }

    if (cancle.includes(keyPressed)) {
        input_field.value = ""
    }

    // 입력 금지
    if (!valid_input.includes(keyPressed) && !enter.includes(keyPressed)) {
        e.preventDefault();
    }
});

input_buttons.forEach(function(button) {
    button.addEventListener("click", function (e) {
        input_field.value += button.textContent;
    });
});