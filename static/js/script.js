setTimeout(function () {
    let messages = document.getElementById("msg");
    let alert = new bootstrap.Alert(messages);
    alert.close();
}, 4000);

let codes = document.getElementsByTagName('pre');

for (const code of codes) {
  code.classList.add('p-2');
  code.classList.add('bg-warning');
  code.classList.add('rounded');
  code.classList.add('bg-opacity-10');
}





