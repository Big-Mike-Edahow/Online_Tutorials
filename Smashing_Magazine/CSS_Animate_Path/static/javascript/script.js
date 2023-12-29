// script.js

// fallback intimation
onload=()=>{
    if(!CSS.registerProperty) {
      document.querySelector('.chart-circle').style.setProperty("cursor", "default"); 
      document.querySelector('figcaption').innerHTML = document.querySelector('figcaption').innerHTML + '<br><span style="color:red">* @property not supported in this browser, so no animation</span>'; 
    } 
  }

  