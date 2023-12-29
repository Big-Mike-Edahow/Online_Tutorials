// script.js

const summaries = document.querySelectorAll(`.withJS`)
summaries.forEach(e=>{
    e.addEventListener('click',openCloseDetails)
})

function openCloseDetails(){
    summaries.forEach(e =>{
        let details = e.parentNode;
        if(details != this.parentNode){
        details.removeAttribute('open')
    }
    })
}

