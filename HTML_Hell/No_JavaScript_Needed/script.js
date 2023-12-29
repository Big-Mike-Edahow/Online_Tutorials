// script.js

document.querySelector("button").addEventListener("click", () => {
  document.querySelector("dialog").showModal();
});

dialog.addEventListener("close", function () {
    console.log(dialog.returnValue);
  });