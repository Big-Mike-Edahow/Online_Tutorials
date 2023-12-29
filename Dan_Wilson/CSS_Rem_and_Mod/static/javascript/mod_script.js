// mod_script.js

[a, b].forEach((el) => {
    el.addEventListener("input", (e) => {
        document.body.style.setProperty(`--${el.id}`, el.value);
        document.querySelector(`output[for="${el.id}"]`).textContent = el.value;
        document.querySelector(`output[for="${el.id}Mod"]`).textContent = el.value;
        result.textContent = getResult();
        resultMod.textContent = getResultMod();
    });
});

result.textContent = getResult();

function getResult() {
    return window.getComputedStyle(demo).rotate;
}

resultMod.textContent = getResultMod();

function getResultMod() {
    return window.getComputedStyle(demoMod).rotate;
}

alert("Come get some ham!")

