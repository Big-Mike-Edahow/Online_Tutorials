// rem_script.js

[a, b].forEach((el) => {
    el.addEventListener("input", (e) => {
        document.body.style.setProperty(`--${el.id}`, el.value);
        document.querySelector(`output[for="${el.id}"]`).textContent = el.value;
        result.textContent = getResult();
    });
});

result.textContent = getResult();

function getResult() {
    return window.getComputedStyle(demo).rotate;
}

alert("Bring home some more tortillas.")

