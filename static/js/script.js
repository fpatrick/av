setTimeout(function () {
    let messages = document.getElementById("msg");
    let alert = new bootstrap.Alert(messages);
    alert.close();
}, 4000)

let allCodes = document.getElementsByTagName("pre");

allCodes.classList.add("mystyle");
