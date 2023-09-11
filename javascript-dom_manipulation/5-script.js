const headerId = document.querySelector("#update_header")
const headerUpdate = document.querySelector("header")

    headerId.addEventListener("click", function(){
    const newText = "New Header!!!"
    headerUpdate.textContent = newText
})
