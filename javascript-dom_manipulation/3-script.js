const toggle_headerId = document.querySelector("#toggle_header");

const headerColor = document.querySelector("header")
//event controler
toggle_headerId.addEventListener("click", function(){

   
if (headerColor.classList.contains("red")) {
    headerColor.classList.remove("red");
    headerColor.classList.add("green");
} else { 
    
    headerColor.classList.contains("green")
    headerColor.classList.remove("green")
    headerColor.classList.add("red")
}
});
