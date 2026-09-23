document.addEventListener("DOMContentLoaded", function(){

const panInput = document.querySelector("input[name='pan']");

if(panInput){

panInput.addEventListener("input", function(){

this.value = this.value.toUpperCase();

});

}

});
