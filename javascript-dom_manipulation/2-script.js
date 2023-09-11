const read_headerId = document.querySelector("#red_header")

const headerColor = document.querySelector("header")

//event controler
read_headerId.addEventListener("click", function(){
// add red class to the header element when the user
//clicks on the tag with id red_eader
    headerColor.classList.add("red")
});
